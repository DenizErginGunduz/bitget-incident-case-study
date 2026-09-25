# Method and limitations

## Scope and selection

This study examines 13 selected transactions associated with the 24 September 2026 Bitget incident. The sample covers an Arbitrum transfer and conversion path, an XRPL payment sequence, and an Optimism/Ethereum address relationship. It is a purposive sample assembled from public research leads, not a complete or statistically representative incident population.

The transaction interval runs from **24 September 19:01:20 UTC to 25 September 02:55:23 UTC**. This is a sample boundary, not the start or end of the incident. Bitget's reported loss and third-party aggregate estimates provide context; neither is independently reconstructed from the selected records.

## Collection and preservation

Public explorer pages and shared Arkham entity views were inspected on 25 September 2026. Transaction observations are recorded with chain, hash, UTC time, asset, amount, parties, result and analytical role in [the evidence register](EVIDENCE_REGISTER.md) and [structured dataset](data/transactions.json).

The official notice and records A2, A5 and X4 were checked again on the same day. Two viewport screenshots and the visible XRPSCAN JSON representation of X4 were retained. The [capture manifest](data/capture-manifest.json) records their source URLs, file-save times and SHA-256 digests. File-save times are filesystem metadata, not trusted timestamp attestations; digests establish file identity, not source authenticity.

Most other observations are preserved as transcribed fields and source links. Exact per-page capture times and full historical Arkham membership pages were not retained. Current explorer labels and entity membership may differ from the recorded observations. No independent node query or cryptographic verification of provider responses was performed.

## Evidence classification

| Class | Meaning in this study | Limitation |
|---|---|---|
| Official statement | What Bitget publicly reported | Not independent confirmation of loss, architecture or cause |
| Explorer observation | Fields or events inspected on a public transaction page | Provider rendering and decoding; not independent node validation |
| Archived explorer representation | X4's visible JSON, retained for offline checks | Includes provider-normalized fields; not an authenticated RPC response |
| Third-party research | Public analyst totals, hypotheses and shared entities | Sources may reuse the same upstream evidence |
| Derived result | Arithmetic or comparison applied to recorded observations | Conditional on input accuracy and the selected population |
| Hypothesis | A proposed explanation or monitoring rule | Requires discriminating evidence or evaluation |

Search results and research summaries supplied discovery leads. Transaction claims are supported by the cited explorer observations; discovery material does not substitute for those observations. Wallet labels are attributed to their providers rather than treated as independently authenticated ownership.

## Accounting and graph rules

- **Selected initial receipts:** A1 and X1/X2/X6 are the sampled external receipts. Their combined value is not presented as a complete incident total.
- **Failed payments:** X4 remains in the behavioral timeline but contributes zero delivered XRP to the receipt sum. Its requested amount is retained separately.
- **Source-account transfers:** X3 and X5 are excluded from the external-receipt total because they move value between the two Bitget-labeled source accounts.
- **Downstream turnover:** Onward transfers, swaps, wrapping and bridge events are not added to initial loss.
- **Asset identity:** A5 is excluded from the canonical-USDT0 graph because its event-emitting contract differs. A repeated amount or shortened-address resemblance does not resolve that difference.
- **Cross-chain continuity:** A4 establishes a source deposit. Its destination remains unresolved until the corresponding execution is matched. E2 is an observed mint with an unmatched source burn in this study.
- **Address relationships:** O1 establishes a value-transfer connection. Common control requires additional evidence, including consideration of service intermediaries.

Amounts are stored as decimal strings. E2 retains only the precision observed in the explorer display and is explicitly marked accordingly. USD figures from external studies retain their source attribution and valuation context; current explorer prices are not substituted for historical prices.

## Reproduction and interpretation

The [offline checker](scripts/reproduce.py) sums the three selected successful XRP receipts, calculates the counterfactual overstatement from adding X4's requested amount, checks selected time intervals and amount differences, and compares the noncanonical contract/address values. For X4 it also reads the archived metadata and checks that the sole affected account's balance decrease equals the recorded fee. Results are recorded in [VALIDATION.md](VALIDATION.md).

The XRP `floor(balance) × 0.9` hypothesis is attributed to [YFarmX](https://yfarmx.com/bitget-postmortem-2026/). Reproducing two equalities does not establish automation or stale-balance causation. A treasury baseline, complete surrounding history and internal authorization records would be needed to distinguish competing explanations.

The lookalike-record and entity-set comparisons are observations within this investigation. No exhaustive prior-art search establishes first discovery. The 8.88% counterfactual is an accounting illustration on this sample, not a measured provider error rate or detector-performance result.

## Unresolved questions

| Priority | Question | Evidence needed | Analytical consequence |
|---|---|---|---|
| 1 | Can the total loss be independently reconciled? | All initial receipts, chain/asset identity, deduplication rules and timestamped prices | Prevents partial scope or downstream turnover from becoming a false total |
| 1 | Does the TRX item belong to the same initial-outflow population? | Source transactions and a consistent classification rule | Resolves a material difference between public estimates |
| 1 | Can the central observations be independently replayed? | Saved node receipts/logs or validated XRPL metadata with block/ledger references | Reduces dependence on explorer rendering |
| 2 | Did the Across deposit complete, refund or partially fill? | Matched destination execution for A4 | Completes one cross-chain edge |
| 2 | Does E2 match the proposed source burn? | CCTP message-level match | Avoids linking movements solely by time and value |
| 2 | Is the XRPL refill sequence abnormal? | Full surrounding history, normal treasury baseline and internal authorization records | Distinguishes incident behavior from routine operations |
| 3 | How much did all swaps return? | Complete execution population and contemporaneous reference prices | Supports aggregate proceeds and slippage analysis |

The selected evidence does not establish exploit root cause, perpetrator identity, national attribution, sanctions status, fiat cash-out, freeze/recovery or the effectiveness of Bitget's internal controls.
