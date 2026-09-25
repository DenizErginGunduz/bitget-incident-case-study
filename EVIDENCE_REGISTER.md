# Evidence register

Thirteen selected transactions. Amounts are in asset units, not current USD. All observations originate from public explorer pages inspected on 25 September 2026. The machine-readable file is a manual transcription of those observations; only X4 has an archived explorer JSON representation in this release.

| ID | UTC date/time | Network | Role | Displayed amount / asset | Result | Source |
|---|---|---|---|---:|---|---|
| A1 | 2026-09-24T19:01:20Z | Arbitrum | selected initial receipt | 19668851.773202 USDT0 | success | [Transaction](https://arbiscan.io/tx/0xd032320ad8a3cddc61ec0db5e6e26a6dcf813243a77b7edc5a65451ade0b84e3) |
| A2 | 2026-09-24T19:34:14Z | Arbitrum | onward transfer | 19668851.77 USDT0 | success | [Transaction](https://arbiscan.io/tx/0xea53170b1468c633bdff136c234efd21b543da3ab4abddb3fcf3bbcbc5175e29) |
| A3 | 2026-09-24T19:36:44Z | Arbitrum | selected swap | 5000000 USDT0 | success | [Transaction](https://arbiscan.io/tx/0x6ceac9f09788e041f78c3f96941a0140cfcff6e5febe73b00e7d6cffabfa4c37) |
| A4 | 2026-09-24T19:49:22Z | Arbitrum | source bridge deposit | 500 ETH | success | [Transaction](https://arbiscan.io/tx/0x7725e4894f379fe96dcbbf52a2f2717c802f2f300314690547a4405801146a20) |
| A5 | 2026-09-24T19:48:37Z | Arbitrum | excluded noncanonical records | 19668851.77 noncanonical ERC20 | success | [Transaction](https://arbiscan.io/tx/0x07bb486af245d53f8823a24c586f97500de6c77d2a3490a2338fdfb35651418d) |
| X1 | 2026-09-24T19:01:32Z | XRPL | selected initial receipt | 2248871.536237 XRP | success | [Transaction](https://xrpscan.com/tx/9926E440BC17F3EE7ACB91DB09A44B9781876B19C6E2D046E5E225F758FB25F4) |
| X2 | 2026-09-24T19:16:20Z | XRPL | selected initial receipt | 91420942.755708 XRP | success | [Transaction](https://xrpscan.com/tx/8DF2ECF67268117A34B89BE9B452D3E888A22CBF03E5C196AD72D8B414A84195) |
| X3 | 2026-09-24T19:28:02Z | XRPL | source account internal | 2000000 XRP | success | [Transaction](https://xrpscan.com/tx/98D32498FC3B15849D27DC7321A1A7C7732647FAD0FA67FACDBB0E3331F4923A) |
| X4 | 2026-09-24T20:28:20Z | XRPL | failed external attempt | 9142093.8 XRP | tecUNFUNDED_PAYMENT | [Transaction](https://xrpscan.com/tx/76474A81759D12B7D98B01C77EB1F5B5E44E345E94BA842482F06010B31EA32C) |
| X5 | 2026-09-24T20:40:02Z | XRPL | source account internal | 2183079.516298 XRP | success | [Transaction](https://xrpscan.com/tx/5DBD1295C3502AFD3B283E0135065B5E41C7FDE73ACE45A6AE94AAC814992308) |
| X6 | 2026-09-24T21:19:21Z | XRPL | selected initial receipt | 9306865.8 XRP | success | [Transaction](https://xrpscan.com/tx/41EFBB55219A89AB33F0E6EAFD3420EE8CBA7F03EC08F8BE546CE5DF5F26D42A) |
| O1 | 2026-09-25T02:49:23Z | Optimism | candidate cluster connection | 495.625 WETH | success | [Transaction](https://optimistic.etherscan.io/tx/0x08ebefeeb9630b5e8948f1e208248865bc5e93bfc0597429a8437bde73d3b125) |
| E2 | 2026-09-25T02:55:23Z | Ethereum | observed mint source unmatched | 1299812.6016 USDC | success | [Transaction](https://etherscan.io/tx/0xe561ab5186cd89309d963f332c048f9eab89028d74d4fedfaf0c78611bd1d9f5) |

**Amount semantics:** X4 delivered zero XRP. A5 is excluded from the canonical-USDT0 graph. A3 has a separate ETH receipt leg. A4 proves only a source deposit. E2 is displayed to limited precision and is not linked here to a source burn. No downstream row is added to the incident loss estimate.

## Address roles and attribution

| Role | Address | Evidence boundary |
|---|---|---|
| Arbitrum source | `0x1AB4973a48dc892Cd9971ECE8e01DcC7688f8F23` | Explorer Bitget label; not independently authenticated ownership |
| Collector | `0x770b10b273fC44Fe9197D6bF20F145c2e98463Ee` | Recipient in A1, sender in A2 |
| Staging | `0xe410a2E5710Ee787bcaa63f52A3943ff71F0d946` | Recipient in A2 and account in A3/A4 |
| XRPL source 1 | `rGDreBvnHrX1get7na3J4oowN19ny4GzFn` | XRPSCAN Bitget (1) label |
| XRPL source 2 | `rwTTsHVUDF8Ub2nzV2oAeWxfJzUvobXLEf` | XRPSCAN Bitget (2) label |
| XRPL external recipient | `rwNhefsz1UQEusxhCvHip3RANinWi4CTck` | Common recipient of X1/X2/X6 |
| Additional cluster candidate | `0x2b03476bC4070e3019B3D5f4EC46edC27284ecd8` | Receipt in O1; common control unproven |

## Shared-entity membership observation

Recorded during the earlier 25 September morning session, approximately 09:15 UTC; these are mutable user-created entity populations, not immutable chain records.

- [Entity A](https://arkm.com/labels/f22a00ea-0a01-41d4-af5d-9e565bb12f37): 26 EVM members.
- [Entity B](https://arkm.com/labels/a4845a2d-0aca-4d28-b0fe-fb986c3370ac): 25 EVM members.
- Observed intersection: 25. A minus B: `0x2b03476bC4070e3019B3D5f4EC46edC27284ecd8`. B minus A: empty.
- The full historical membership pages were not archived in this public release. This comparison therefore has weaker preservation than the immutable transaction references; reviewers should not assume current membership is unchanged.

## Claim classification

| Claim | Status | What could change the conclusion? |
|---|---|---|
| X4 transferred no XRP to the destination | Explorer metadata supported | Conflicting authoritative ledger metadata |
| A5 is not a canonical-USDT0 movement | Contract mismatch observed | Incorrect transcription of chain or contract |
| O1 links two addresses by value transfer | Explorer observed | Conflicting receipt or asset identity |
| Those addresses share control | Not established | Independent control evidence, accounting for service intermediaries |
| A4 completed on Ethereum | Unresolved in this release | Matched destination execution |
| The whole incident totals $351.6m on-chain | Not independently reproduced | Complete deduplicated initial-outflow inventory and historical prices |
