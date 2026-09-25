# Reproduction results

Checked 25 September 2026 using Python 3.12.14. The offline checker completed successfully against the retained explorer representations and capture manifest.

```text
Scope: offline checks of a selected explorer-observed sample.
Successful selected XRP receipts from archived delivered_amount: 102976680.091945 XRP
Failed requested amount excluded: 9142093.8 XRP
If wrongly added: 112118773.891945 XRP; overstatement 8.8778%
X4 archived balance decrease: 20 drops; matches fee only
Source 2 continuity: 8 AccountRoot updates; 7 balance and predecessor links matched.
D1/D2/D3: 10 drops each; all interval balance changes reconcile with delivery and fees.
Source 2 balance after X6: 1034096.244661 XRP
X2/X3/X4/X6 share a SigningPubKey; authorization and compromise mechanism are not established.
A1 to A2: 1974 seconds; amount difference 0.003202 USDT0
X4 to X5: 702 seconds; X5 to X6: 2359 seconds
Two floor(balance) x 0.9 equalities reproduced; this does not establish causation.
Noncanonical token and lookalike-address distinctions: passed.
Arkham public label sets: 26 and 25; 25 shared and O1 destination is the sole difference.
Archive digests: 19 files verified.
No node query, ownership attribution, detection-performance test or complete loss reconciliation performed.
```

The checker reads nine archived XRPSCAN Raw JSON views. It verifies the three successful external receipts from `meta.delivered_amount`, X4's fee-only failure, and source 2's eight AccountRoot updates from X2 through X6. All seven adjacent balance pairs and predecessor transaction/ledger references match; delivered amounts and fees explain each balance change. D1–D3 account for the three 10-drop increments.

It also reproduces the two archived Arkham address sets and verifies SHA-256 digests for all 19 retained evidence files. Local document and image links resolve. The walkthrough's source-2 balance table was compared with the archived metadata, and the transaction register was checked against all 16 structured records.

These are consistency and preservation checks. They do not authenticate provider data, establish common control, measure detector performance, reconcile the complete incident loss, or match the outstanding bridge endpoints.
