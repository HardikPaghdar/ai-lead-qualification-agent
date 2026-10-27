# AI Lead Qualification Agent

A small, runnable lead-scoring demo for teams that need a transparent first-pass triage before a human sales conversation.

## What it does
- Scores each lead from budget, delivery timeline, company size, and specificity of the stated need.
- Returns a 0–100 score, tier, evidence-based reasons, and a suggested next action.
- Sorts a batch of leads from highest to lowest score.
- Uses deterministic rules so a sales team can explain and tune the result.

> This is a qualification rules engine, not an LLM or CRM integration. The score is a demo heuristic, not a validated predictor of conversion. Review decisions with a person.

## Run it
Requires Python 3.10+; no runtime dependencies.

```bash
python - <<'PY'
import json
from app import qualify_many
leads = json.load(open("examples/leads.json", encoding="utf-8"))
for item in qualify_many(leads):
    print(item["score"], item["tier"], item["lead"]["company"])
PY
```

## Test
```bash
python -m unittest discover -s tests -v
```

## Scoring model
Budget contributes up to 30 points, timeline up to 25, company size up to 20, and need clarity up to 25. Thresholds are intentionally simple and visible in `app.py`; adapt them to your own sales process before using real data.

## Project layout
- `app.py` — scoring logic
- `examples/leads.json` — synthetic sample leads
- `tests/` — regression tests
- `.github/workflows/ci.yml` — automated tests on pushes and pull requests

## Next steps
Add CRM adapters behind an interface, calibration against historical outcomes, audit logging, and access controls before handling customer data. Never use this score as the sole basis for high-impact decisions.

## Explore more

- [Agentic Sales Outreach Copilot](https://github.com/HardikPaghdar/agentic-sales-outreach-copilot) — drafts outreach for human review.
- [LLM Cost Optimization Gateway](https://github.com/HardikPaghdar/llm-cost-optimization-gateway) — policy-based model selection prototype.
- [More projects on my portfolio](https://hardikpaghdar.netlify.app/).
