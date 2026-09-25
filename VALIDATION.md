# Reproduction results

Checked 2026-09-25 12:14 UTC using Python 3.12.14.

The offline checker completed successfully. Both viewport screenshots were visually checked against the corresponding transaction observations during collection.

```text
Scope: offline checks of a selected, manually transcribed explorer sample.
Successful selected XRP receipts: 102976680.091945 XRP
Failed requested amount excluded: 9142093.8 XRP
If wrongly added: 112118773.891945 XRP; overstatement 8.8778%
X4 archived balance decrease: 20 drops; matches fee only
A1 to A2: 1974 seconds; amount difference 0.003202 USDT0
X4 to X5: 702 seconds; X5 to X6: 2359 seconds
Two floor(balance) x 0.9 equalities reproduced; this does not establish causation.
Noncanonical token and lookalike-address distinctions: passed.
No node query, ownership attribution, detection-performance test or complete loss reconciliation performed.
```

These checks establish internal consistency of the selected arithmetic and archived metadata. They do not authenticate explorer data, establish detector performance or replace independent review.
