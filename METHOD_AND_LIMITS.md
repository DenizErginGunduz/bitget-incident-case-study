# Method, limits and publication review

## Research status

This is a publishable **bounded, early investigation note and teaching case**. It is not a complete forensic reconstruction or a validated detection product. Its professional standard depends on maintaining that scope: each material claim has an identifiable source, direct observations are distinguished from interpretation, and unresolved work is visible.

The underlying record was collected on 25 September 2026 through public explorers and a free authenticated Arkham session. The selected transaction interval is 24 September 19:01:20 UTC through 25 September 02:55:23 UTC. That is a sample boundary, not the start/end of the incident. This release does not attempt to incorporate every later public update.

During the publication review, the official notice and A2/A5/X4 were reopened. Two viewport screenshots and X4's visible Raw JSON representation were preserved. Most other transaction observations are retained as manually transcribed fields and source links; exact per-page capture times were not logged during the earlier work. No fabricated precision is added retrospectively.

## Evidence hierarchy

| Class | Meaning here | Limitation |
|---|---|---|
| Official statement | What Bitget publicly reported | Not independent confirmation of loss, architecture or cause |
| Explorer observation | Fields or events inspected on a public transaction page | Provider rendering/decoding; not independent node validation |
| Archived explorer representation | X4's visible JSON, retained for offline checks | Includes provider-normalized fields; not an authenticated RPC response |
| Third-party research | Public analyst totals, hypotheses and shared entities | Attribution required; may reuse the same upstream source |
| Our derivation | Arithmetic or comparison performed on those observations | Only as sound as the inputs and selected population |
| Hypothesis | A proposed explanation or monitoring rule | Requires discriminating evidence or evaluation |

AI-assisted search supplied leads. The Grok responses are not treated as evidence and are not republished. AI assistance was also used to organize, draft and check this release. Explorer inspection does not remove the need for independent review.

## What the research contributes

1. **A concrete settlement/accounting distinction.** The failed XRP request creates a calculable 8.88% overstatement if added to the selected successful external receipts. This is our derived example, not a discovery of missing incident funds.
2. **A worked graph-contamination example.** The canonical and noncanonical contract/address pairs are linked and compared explicitly. The conclusion concerns evidence quality, not the identity or intent of the extra transaction's author.
3. **A conservative cluster-extension example.** A user-entity difference is tested against a direct WETH transfer. It becomes a review lead with provenance, not a common-owner conclusion.
4. **A teachable stopping rule.** Source bridge evidence is preserved without pretending an unmatched destination has been verified.

These are useful analytical contributions. There is no established claim of first discovery, new perpetrator attribution, undisclosed loss or recovered value. The XRP 90% pattern is credited to YFarmX. The research has not surveyed all X posts, private reports or commercial-provider findings, so uniqueness cannot be asserted.

## Why the earlier draft needed strengthening

- The detailed Arbitrum example could be mistaken for the whole event. The release now opens with incident scale and a selected-sample boundary.
- “Verified” could suggest node-backed reproduction. This release instead names the verification level and provides one archived explorer representation.
- Narrative findings were difficult to audit. Stable evidence IDs, structured decimal fields, source links and a small checker now connect claims to inputs.
- The practical value was implied. The walkthrough explains the question, inspection and stopping condition; the monitoring note states an evaluation plan.
- A broad claim of originality would have exceeded the evidence. Discovery, replication, derivation and unresolved interpretation are now separated.

## Remaining gaps and priority

| Priority | Open question | Evidence needed | Why it matters |
|---|---|---|---|
| 1 | Can the total loss be independently reconciled? | All initial receipts, chain/asset identity, deduplication rules and timestamped prices | Prevents partial scope or downstream turnover from becoming a false total |
| 1 | Does the TRX item belong to the same initial-outflow population? | Source transactions and a consistent classification rule | Explains a material difference between public estimates |
| 1 | Can the central observations be independently replayed? | Saved node receipts/logs or validated XRPL metadata with block/ledger references | Reduces dependence on live explorer rendering |
| 2 | Did the Across deposit complete, refund or partially fill? | Matched destination execution for A4 | Completes one cross-chain edge |
| 2 | Does E2 match the proposed source burn? | CCTP message-level match | Avoids linking nearby movements only by time and value |
| 2 | Is the XRPL refill sequence abnormal? | Full surrounding history, normal treasury baseline and internal authorization records | Distinguishes incident behavior from routine operations |
| 3 | How much did all swaps return? | Complete execution population and contemporaneous reference prices | Supports aggregate proceeds/slippage analysis |

No conclusion is made about exploit root cause, named perpetrators, a particular country's involvement, sanctions status, fiat cash-out, freeze/recovery or the effectiveness of Bitget's internal controls. Those require different evidence.

## Privacy and distribution decision

The public package contains public transaction identifiers, public wallet addresses, attributed labels, original analysis and public explorer excerpts. It contains no user account details, customer/KYC data, credentials, private keys, internal Bitget records, private correspondence, job-search information or local session logs. Public signing keys/signatures in the archived XRPL transaction are public ledger data; they are not wallet secrets.

There is consequently no identified sensitive dataset requiring a private companion repository for **this package**. Working chat transcripts and personal workspace files are excluded. Unsupported identity allegations and private leads are excluded too. This is a content review, not a claim that every possible re-identification risk has been eliminated.

If later research obtains non-public records, keep them in a separately controlled private repository and publish only reviewed extracts. Do not temporarily put secrets or private records into a public branch: Git history and forks can retain them. A public pull request is public as well.

No permissive license is assigned to third-party screenshots or data. Attribution and original source links remain with each excerpt; this repository does not grant rights over provider material.
