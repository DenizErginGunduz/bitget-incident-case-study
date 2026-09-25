# Screenshot and data provenance

Both images are genuine browser screenshots of public, signed-out explorer views, saved on **25 September 2026 during the publication review**. File-save times and digests are recorded in `../data/capture-manifest.json`; those times are local filesystem metadata, not trusted capture attestations. The images show the visible viewport; no labels, amounts or transaction fields were edited. They are illustrative excerpts rather than authenticated ledger evidence.

| File | Source | What it shows |
|---|---|---|
| `arb-lookalike-record.png` | [Arbiscan A5](https://arbiscan.io/tx/0x07bb486af245d53f8823a24c586f97500de6c77d2a3490a2338fdfb35651418d) | Different contract and one repeated-amount/lookalike transfer row |
| `xrp-failed-payment.png` | [XRPSCAN X4](https://xrpscan.com/tx/76474A81759D12B7D98B01C77EB1F5B5E44E345E94BA842482F06010B31EA32C) | Failed requested payment and fee-only source balance change |

`../data/explorer/xrpl-failed-payment.json` is the text shown in XRPSCAN's expanded **Raw JSON** panel, read from the visible page and saved verbatim with a trailing newline. It is an explorer representation, not a fresh node RPC response. In that representation `Fee` is a number in drops and `Amount` is a string in drops; scripts should not assume every provider uses identical JSON types.

The selected viewport positions omit account menus; some public navigation and advertising remain visible. Hashes in the manifest establish the identity of saved files for later comparison; they do not prove source authenticity or a trusted capture timestamp. Source provider names and links are retained for attribution. No reuse rights over provider material are granted by this repository.
