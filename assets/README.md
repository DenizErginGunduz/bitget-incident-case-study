# Screenshot and data provenance

The images are browser screenshots of public explorer and Arkham label views, saved on **25 September 2026**. File-save times and digests are recorded in `../data/capture-manifest.json`; those times are local filesystem metadata, not trusted capture attestations. The images show visible viewports; no labels, amounts or transaction fields were edited. They are illustrative excerpts rather than authenticated ledger evidence.

| File | Source | What it shows |
|---|---|---|
| `arb-lookalike-record.png` | [Arbiscan A5](https://arbiscan.io/tx/0x07bb486af245d53f8823a24c586f97500de6c77d2a3490a2338fdfb35651418d) | Different contract and one repeated-amount/lookalike transfer row |
| `arb-lookalike-reverse.png` | [Arbiscan A5](https://arbiscan.io/tx/0x07bb486af245d53f8823a24c586f97500de6c77d2a3490a2338fdfb35651418d) | Second repeated-amount row, from the collector lookalike to the actual staging address |
| `xrp-failed-payment.png` | [XRPSCAN X4](https://xrpscan.com/tx/76474A81759D12B7D98B01C77EB1F5B5E44E345E94BA842482F06010B31EA32C) | Failed requested payment and fee-only source balance change |
| `arkham-entity-a-top.png`, `arkham-entity-a-middle.png`, `arkham-entity-a-bottom.png` | [Arkham entity A](https://arkm.com/labels/f22a00ea-0a01-41d4-af5d-9e565bb12f37) | Overlapping views of the public 26-address EVM list |
| `arkham-entity-b-top.png`, `arkham-entity-b-middle.png`, `arkham-entity-b-bottom.png` | [Arkham entity B](https://arkm.com/labels/a4845a2d-0aca-4d28-b0fe-fb986c3370ac) | Overlapping views of the public 25-address EVM list |

`../data/explorer/xrpl-*.json` files are text shown in XRPSCAN's expanded **Raw JSON** panel, read from the visible pages and saved with a trailing newline. The X4 filename is `xrpl-failed-payment.json`. They are explorer representations, not fresh node RPC responses. In those representations `Fee` is a number in drops and `Amount` is a string in drops; scripts should not assume every provider uses identical JSON types. `../data/arkham-entity-membership.json` records the two full address lists extracted from the public label views; compare addresses case-insensitively.

The selected viewport positions omit account menus; some public navigation and advertising remain visible. Hashes in the manifest establish the identity of saved files for later comparison; they do not prove source authenticity or a trusted capture timestamp. Source provider names and links are retained for attribution. No reuse rights over provider material are granted by this repository.
