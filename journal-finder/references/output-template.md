# Output Template

## Recommended Report Sections

1. **Recommendation Summary**
   - Top 3 targets, why they fit, and the direct submission strategy.

2. **Ranked Journal Table**
   - Journal name
   - Publisher/society
   - SCI/SCIE status
   - CAS partition
   - JCR quartile
   - latest impact factor
   - aims & scope fit
   - field recognition
   - workload/risk
   - physical/hardware requirement
   - recommendation
   - source links

3. **Similar Articles**
   - 2-4 per strong target when possible.
   - Include title, DOI/link, similarity, and gap relative to the user's manuscript.

4. **Open Special Issues**
   - Venue, title, deadline, link, eligibility, and whether it satisfies hard constraints.
   - Keep expired calls separate or omit them unless they clarify strategy.

5. **Revision Checklist**
   - Desk-reject blockers
   - Scope/framing changes
   - Baselines and ablations
   - Statistical analysis
   - Physical/hardware or real-world validation
   - Data/code/reproducibility
   - Article length/style constraints

## Default Scoring

Use a 0-100 score for each dimension:

- Topical fit: 35%
- Field recognition: 25%
- Metrics/ranking: 20%
- Lower workload/risk: 15%
- Open special issue fit: 5%

Never let an open special issue override a hard index/ranking requirement. If a journal fails a hard constraint, put it in `Backup` or `Not Recommended`.
