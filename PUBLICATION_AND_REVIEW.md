# Publication and external-review brief

## Publication positioning

Use the repository as the evidence reference. A short LinkedIn post can explain one result and link to the worked guide. An X thread can then show the two explorer comparisons. Lead with the research question and observable finding; do not market this release as a full $351.6m reconstruction or a newly discovered attack vector.

Suggested post, ready to adapt after independent critique:

> A transaction amount is not always a delivered payment, and a transfer row is not automatically a trustworthy graph edge.
>
> In a bounded review of the September 2026 Bitget incident, I examined a failed XRP payment, lookalike token-transfer records and a difference between two shared address clusters.
>
> One concrete result: adding a failed 9.14m XRP request to the selected successful receipts would overstate that sample by 8.88%. The repository shows the calculation, source transactions and an explorer walkthrough.
>
> This is an early evidence-quality case study, with explicit gaps. It does not claim a complete loss reconstruction or perpetrator attribution. The earlier XRP amount-pattern hypothesis is credited to YFarmX.
>
> Read the investigation: https://github.com/DenizErginGunduz/bitget-incident-case-study

This post has not been submitted to any social platform. Do not imply that the illustrative accounting error occurred in a named analytics product.

## Independent AI or human review prompt

Copy the following prompt and provide the repository URL or the complete files. Ask reviewers to work independently before sharing other reviewers' conclusions.

```text
Act as a skeptical reviewer of an early on-chain investigation intended for a professional AML/fraud research portfolio.

Review https://github.com/DenizErginGunduz/bitget-incident-case-study and its linked source transactions. Do not assume the author or another AI has verified a claim merely because it appears in a table.

Assess:
1. Does every material claim stay within its evidence? Distinguish official statements, explorer observations, archived representations, our calculations and hypotheses.
2. Reproduce the selected XRP sum, failed-payment exclusion, 8.88% counterfactual overstatement, time intervals and the floor(balance) x 0.9 equalities. Explain what those calculations do and do not prove.
3. Does the canonical/noncanonical token comparison support exclusion from the USDT0 graph? Are ownership, intent or novelty overstated?
4. Is the Arkham membership comparison adequately preserved? Does the WETH receipt support anything beyond a transfer connection?
5. Are bridge completion, valuation, sampling and full-loss reconciliation boundaries accurate and visible?
6. Would a compliance or fraud reviewer learn an actionable method? Identify any generic filler, missing counterexample or untested detection claim.
7. Identify privacy, attribution or reputational problems in the actual published content, without inventing hypothetical private data.

Return findings ordered by severity. For each, cite the file/section, the exact claim, supporting source, why it matters, and a concrete correction. Separately list facts you could not independently verify. Do not call unavailable evidence false merely because you could not access it. Do not invent transaction details, test results or first-discovery claims.

Conclude with one of: publish as scoped; publish after specific corrections; or hold. Explain whether the work contributes an original empirical discovery, a replication, a useful methodological synthesis, or some combination. Do not flatter the author.
```

## Review disposition

Independent external critique has **not** yet been completed. Log factual corrections in a dated change note, rerun the checker when numerical inputs change, and keep prior claims traceable through Git history. A later review should not silently expand this release's sample or claim to validate parts it did not inspect.
