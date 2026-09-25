"""Offline arithmetic and one archived explorer-metadata check; not chain validation."""
import json
from decimal import Decimal, ROUND_FLOOR
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = Decimal

def require(condition, message):
    if not condition:
        raise ValueError(message)

def main():
    data = json.loads((ROOT / 'data/transactions.json').read_text(encoding='utf-8'))
    records = data['records']
    rows = {r['id']: r for r in records}
    require(len(rows) == len(records) == 13, 'Unexpected or duplicate record IDs')
    require(len({(r['chain'], r['tx_hash']) for r in records}) == 13, 'Duplicate transaction')
    selected = [r for r in records if r['chain'] == 'XRPL' and r['role'] == 'selected_initial_receipt']
    require({r['id'] for r in selected} == {'X1', 'X2', 'X6'}, 'Unexpected XRP receipt population')
    require(all(r['result'] == 'success' for r in selected), 'Failed payment in receipt total')
    total = sum((D(r['delivered_amount']) for r in selected), D(0))
    requested = D(rows['X4']['amount'])
    require(total == D('102976680.091945'), 'XRP receipt sum changed')

    raw = json.loads((ROOT / rows['X4']['archived_explorer_json']).read_text(encoding='utf-8'))
    require(raw['hash'] == rows['X4']['tx_hash'], 'Archived hash mismatch')
    require(raw['Account'] == rows['X4']['source'] and raw['Destination'] == rows['X4']['destination'], 'Archived parties mismatch')
    require(raw['meta']['TransactionResult'] == 'tecUNFUNDED_PAYMENT', 'Archived result mismatch')
    require(D(raw['Amount']) / D(1000000) == requested, 'Requested amount mismatch')
    nodes = raw['meta']['AffectedNodes']
    require(len(nodes) == 1 and 'ModifiedNode' in nodes[0], 'Review unexpected affected nodes')
    node = nodes[0]['ModifiedNode']
    require(node['LedgerEntryType'] == 'AccountRoot' and node['FinalFields']['Account'] == raw['Account'], 'Unexpected affected account')
    delta_drops = D(node['PreviousFields']['Balance']) - D(node['FinalFields']['Balance'])
    require(delta_drops == D(raw['Fee']) == D(20), 'Balance change is not the recorded fee')

    def seconds(a, b):
        parse = lambda id: datetime.fromisoformat(rows[id]['timestamp_utc'].replace('Z', '+00:00'))
        return int((parse(b) - parse(a)).total_seconds())
    floor90 = lambda value: D(value).to_integral_value(rounding=ROUND_FLOOR) * D('0.9')
    require(floor90(rows['X2']['source_balance_after']) == requested, 'Earlier-balance pattern changed')
    require(floor90(rows['X6']['source_balance_before']) == D(rows['X6']['amount']), 'Later-balance pattern changed')
    require(rows['A1']['token_contract'].lower() == rows['A2']['token_contract'].lower(), 'Canonical transfer contracts differ')
    require(rows['A5']['token_contract'].lower() != rows['A2']['token_contract'].lower(), 'Excluded contract is not distinct')
    require(rows['A5']['lookalike_collector'].lower() != rows['A2']['source'].lower(), 'Collector lookalike not distinct')
    require(rows['A5']['lookalike_staging'].lower() != rows['A2']['destination'].lower(), 'Staging lookalike not distinct')

    print('Scope: offline checks of a selected, manually transcribed explorer sample.')
    print(f'Successful selected XRP receipts: {total} XRP')
    print(f'Failed requested amount excluded: {requested} XRP')
    print(f'If wrongly added: {total + requested} XRP; overstatement {requested / total * 100:.4f}%')
    print(f'X4 archived balance decrease: {delta_drops} drops; matches fee only')
    print(f'A1 to A2: {seconds("A1", "A2")} seconds; amount difference {D(rows["A1"]["amount"]) - D(rows["A2"]["amount"])} USDT0')
    print(f'X4 to X5: {seconds("X4", "X5")} seconds; X5 to X6: {seconds("X5", "X6")} seconds')
    print('Two floor(balance) x 0.9 equalities reproduced; this does not establish causation.')
    print('Noncanonical token and lookalike-address distinctions: passed.')
    print('No node query, ownership attribution, detection-performance test or complete loss reconciliation performed.')

if __name__ == '__main__':
    main()
