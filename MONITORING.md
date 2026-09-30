# From a case observation to a monitoring question

The case supports concrete investigation requirements. It does not establish detector accuracy, a universal threshold or that a rule would have prevented the incident.

| Scenario | Evidence to retain | Why retain it? | Plausible benign explanation / limitation |
|---|---|---|---|
| Large external payment fails, source is refilled, external payment later succeeds | Both successful and failed transactions, requested/delivered values, balances and timing | Connects attempts and subsequent execution without inflating loss | Routine treasury refills and customer withdrawals can have a similar sequence |
| Receipt is forwarded, converted and submitted to a bridge | Asset identity, account-level movements, execution roles and source event identifiers | Preserves a sequence across changes in asset and chain | Treasury rebalancing and market-making can also do this |
| Token history contains repeated amounts and lookalike addresses | Full addresses, chain, event-emitting contract and transaction result | Prevents unqualified rows from becoming canonical-asset edges | A suspicious row alone does not identify its author or motive |
| Public entities disagree about an address | Dated set membership, edge evidence and service-counterparty context | Makes analyst grouping decisions reviewable | Shared labels may copy each other; receipt does not imply common control |

## Evaluation design

In this sample, X4 fails at 20:28:20 UTC, X5 refills the account 11 minutes 42 seconds later, and X6 succeeds a further 39 minutes 19 seconds later. Those intervals define a sequence worth reviewing; they do not prove that an alert or intervention would have been possible.

For an exchange transaction-monitoring team, compare a large-successful-outflow baseline with a rule that also preserves failed attempts and correlates subsequent refills. Freeze a review window, thresholds and a normal-period sample **before** evaluating outcomes. No calibrated threshold is supplied by this one incident.

Record what information was actually available at each event time. Today's “exploiter” labels must not be used as historical features. Allowlisted treasury addresses must also be reconstructed as of the evaluation time, rather than inferred from later knowledge.

Evaluate at an equal analyst-review budget. Measure additional actionable cases, false positives on normal treasury activity, time to first useful alert, and review time. “More alerts” and “more value covered” are not proof of improved detection. An investigation's final disposition should be separately adjudicated.

For data-quality controls, measure how often unqualified records would have entered the canonical-asset graph and how often genuine transfers are wrongly excluded. Include legitimate uncommon tokens and contract-mediated transfers; an allowlist-only filter may trade contamination for missed activity.

## What a compliance analyst can ask next

- Does an observed recipient have independently supported exposure to a regulated service, and what information can that service lawfully provide?
- Is a transfer direct, indirect or merely an unsupported cluster association? Preserve hop depth and asset continuity.
- Which evidence supports escalation, and which fields are still provider labels or hypotheses?
- Could the same rule flag ordinary treasury or customer activity? What evidence would distinguish the cases?

The case is relevant to fraud investigation and transaction-monitoring design. It does not, by itself, establish money laundering or a legal reporting obligation for any particular institution.
