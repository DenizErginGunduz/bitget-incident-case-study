"""Offline checks of archived explorer observations; not node validation."""
import hashlib
import json
from datetime import datetime
from decimal import Decimal, ROUND_FLOOR
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = Decimal
DROPS = D(1_000_000)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def account_balances(raw, address):
    for wrapper in raw['meta']['AffectedNodes']:
        node = next(iter(wrapper.values()))
        final = node.get('FinalFields', {})
        if node.get('LedgerEntryType') == 'AccountRoot' and final.get('Account') == address:
            previous = node.get('PreviousFields', {}).get('Balance')
            return (D(previous) if previous is not None else None, D(final['Balance']))
    raise ValueError(f'No AccountRoot balance change for {address}')


def main():
    data = json.loads((ROOT / 'data/transactions.json').read_text(encoding='utf-8'))
    records = data['records']
    rows = {r['id']: r for r in records}
    require(len(rows) == len(records) == 13, 'Unexpected or duplicate record IDs')
    require(len({(r['chain'], r['tx_hash']) for r in records}) == 13, 'Duplicate transaction')

    archived = {}
    for id in ('X1', 'X2', 'X4', 'X5', 'X6'):
        row = rows[id]
        raw = json.loads((ROOT / row['archived_explorer_json']).read_text(encoding='utf-8'))
        require(raw['hash'] == row['tx_hash'], f'{id}: hash mismatch')
        require(raw['TransactionType'] == 'Payment', f'{id}: not a payment')
        require(raw['Account'] == row['source'] and raw['Destination'] == row['destination'], f'{id}: parties mismatch')
        require(D(raw['Amount']) / DROPS == D(row['amount']), f'{id}: requested amount mismatch')
        expected_result = 'tesSUCCESS' if row['result'] == 'success' else row['result']
        require(raw['meta']['TransactionResult'] == expected_result, f'{id}: result mismatch')
        if id != 'X4':
            delivered = D(raw['meta']['delivered_amount']) / DROPS
            require(delivered == D(row['delivered_amount']), f'{id}: delivered amount mismatch')
        archived[id] = raw

    selected = [r for r in records if r['chain'] == 'XRPL' and r['role'] == 'selected_initial_receipt']
    require({r['id'] for r in selected} == {'X1', 'X2', 'X6'}, 'Unexpected XRP receipt population')
    total = sum((D(archived[r['id']]['meta']['delivered_amount']) / DROPS for r in selected), D(0))
    requested = D(rows['X4']['amount'])
    require(total == D('102976680.091945'), 'XRP receipt sum changed')

    failed = archived['X4']
    require(len(failed['meta']['AffectedNodes']) == 1, 'Unexpected affected nodes for X4')
    before, after = account_balances(failed, rows['X4']['source'])
    delta_drops = before - after
    require(delta_drops == D(failed['Fee']) == D(20), 'X4 balance change is not fee only')
    require(before / DROPS == D(rows['X4']['source_balance_before']), 'X4 opening balance mismatch')
    require(after / DROPS == D(rows['X4']['source_balance_after']), 'X4 ending balance mismatch')

    _, x2_after = account_balances(archived['X2'], rows['X2']['source'])
    require(x2_after / DROPS == D(rows['X2']['source_balance_after']), 'X2 ending balance mismatch')
    x5_before, x5_after = account_balances(archived['X5'], rows['X5']['destination'])
    require(x5_before == after, 'X4-to-X5 selected account balance mismatch')
    require(x5_after / DROPS == D(rows['X5']['destination_balance_after']), 'X5 ending balance mismatch')
    x6_before, _ = account_balances(archived['X6'], rows['X6']['source'])
    require(x6_before / DROPS == D(rows['X6']['source_balance_before']), 'X6 opening balance mismatch')
    gap_drops = x6_before - x5_after
    require(gap_drops == 10, 'Review intervening X5-to-X6 balance change')

    def seconds(a, b):
        parse = lambda id: datetime.fromisoformat(rows[id]['timestamp_utc'].replace('Z', '+00:00'))
        return int((parse(b) - parse(a)).total_seconds())

    floor90 = lambda drops: (drops / DROPS).to_integral_value(rounding=ROUND_FLOOR) * D('0.9')
    require(floor90(x2_after) == requested, 'Earlier-balance pattern changed')
    require(floor90(x6_before) == D(rows['X6']['amount']), 'Later-balance pattern changed')
    require(rows['A1']['token_contract'].lower() == rows['A2']['token_contract'].lower(), 'Canonical contracts differ')
    require(rows['A5']['token_contract'].lower() != rows['A2']['token_contract'].lower(), 'Excluded contract is not distinct')
    require(rows['A5']['lookalike_collector'].lower() != rows['A2']['source'].lower(), 'Collector lookalike not distinct')
    require(rows['A5']['lookalike_staging'].lower() != rows['A2']['destination'].lower(), 'Staging lookalike not distinct')

    labels = json.loads((ROOT / 'data/arkham-entity-membership.json').read_text(encoding='utf-8'))
    a = {address.lower() for address in labels['entity_a']['evm_addresses']}
    b = {address.lower() for address in labels['entity_b']['evm_addresses']}
    require(len(a) == 26 and len(b) == 25 and len(a & b) == 25, 'Arkham label set counts changed')
    require(a - b == {rows['O1']['destination'].lower()} and not b - a, 'Arkham label set difference changed')

    manifest = json.loads((ROOT / 'data/capture-manifest.json').read_text(encoding='utf-8'))
    for item in manifest['files']:
        path = ROOT / item['path']
        require(path.is_file(), f'Missing archived file: {item["path"]}')
        require(hashlib.sha256(path.read_bytes()).hexdigest() == item['sha256'], f'Digest mismatch: {item["path"]}')

    print('Scope: offline checks of a selected explorer-observed sample.')
    print(f'Successful selected XRP receipts from archived delivered_amount: {total} XRP')
    print(f'Failed requested amount excluded: {requested} XRP')
    print(f'If wrongly added: {total + requested} XRP; overstatement {requested / total * 100:.4f}%')
    print(f'X4 archived balance decrease: {delta_drops} drops; matches fee only')
    print(f'X5 ending to X6 opening balance difference: +{gap_drops} drops; cause unresolved')
    print(f'A1 to A2: {seconds("A1", "A2")} seconds; amount difference {D(rows["A1"]["amount"]) - D(rows["A2"]["amount"])} USDT0')
    print(f'X4 to X5: {seconds("X4", "X5")} seconds; X5 to X6: {seconds("X5", "X6")} seconds')
    print('Two floor(balance) x 0.9 equalities reproduced; this does not establish causation.')
    print('Noncanonical token and lookalike-address distinctions: passed.')
    print('Arkham public label sets: 26 and 25; 25 shared and O1 destination is the sole difference.')
    print(f'Archive digests: {len(manifest["files"])} files verified.')
    print('No node query, ownership attribution, detection-performance test or complete loss reconciliation performed.')


if __name__ == '__main__':
    main()
