# Reproduction results

Checked 25 September 2026 using Python 3.12.14. The offline checker completed successfully against the retained explorer representations and capture manifest.

```text
Scope: offline checks of a selected explorer-observed sample.
Successful selected XRP receipts from archived delivered_amount: 102976680.091945 XRP
Failed requested amount excluded: 9142093.8 XRP
If wrongly added: 112118773.891945 XRP; overstatement 8.8778%
X4 archived balance decrease: 20 drops; matches fee only
X5 ending to X6 opening balance difference: +10 drops; cause unresolved
A1 to A2: 1974 seconds; amount difference 0.003202 USDT0
X4 to X5: 702 seconds; X5 to X6: 2359 seconds
Two floor(balance) x 0.9 equalities reproduced; this does not establish causation.
Noncanonical token and lookalike-address distinctions: passed.
Arkham public label sets: 26 and 25; 25 shared and O1 destination is the sole difference.
Archive digests: 15 files verified.
No node query, ownership attribution, detection-performance test or complete loss reconciliation performed.
```

The checker reads five archived XRPSCAN Raw JSON views, verifies the selected receipt total from `meta.delivered_amount`, checks X4's fee-only failure, and compares the X5 and X6 account balances. The unexplained 10-drop gap is retained explicitly rather than filled by assumption. It also compares the two archived Arkham address lists case-insensitively and verifies SHA-256 digests of the 15 retained files. These are internal consistency and preservation checks, not independent authentication of the providers' data.
