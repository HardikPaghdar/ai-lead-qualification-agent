"""Rule-based lead qualification demo; no external CRM or LLM required."""
from dataclasses import dataclass, asdict
from typing import Any

@dataclass
class Lead:
    name: str
    company: str
    role: str
    need: str
    budget_usd: int
    timeline_days: int
    company_size: int
    source: str = "unknown"

def qualify_lead(raw: dict[str, Any]) -> dict[str, Any]:
    """Score a lead transparently from explicit fit signals (0-100)."""
    lead = Lead(**raw)
    score = 0
    reasons = []
    if lead.budget_usd >= 10000:
        score += 30; reasons.append("budget is at least $10,000")
    elif lead.budget_usd >= 3000:
        score += 18; reasons.append("budget is at least $3,000")
    else:
        reasons.append("budget is below $3,000")
    if lead.timeline_days <= 30:
        score += 25; reasons.append("timeline is within 30 days")
    elif lead.timeline_days <= 90:
        score += 15; reasons.append("timeline is within 90 days")
    else:
        reasons.append("timeline is longer than 90 days")
    if lead.company_size >= 50:
        score += 20; reasons.append("company has 50+ employees")
    elif lead.company_size >= 10:
        score += 12; reasons.append("company has 10+ employees")
    if len(lead.need.strip()) >= 40:
        score += 25; reasons.append("business need includes useful detail")
    elif len(lead.need.strip()) >= 15:
        score += 15; reasons.append("business need is partially defined")
    else:
        reasons.append("business need needs clarification")
    tier = "priority" if score >= 70 else "review" if score >= 40 else "nurture"
    return {"lead": asdict(lead), "score": score, "tier": tier, "reasons": reasons,
            "recommended_next_step": {"priority":"Offer a discovery call within one business day",
            "review":"Ask one or two qualification questions", "nurture":"Share a relevant resource and revisit later"}[tier]}

def qualify_many(leads: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted((qualify_lead(item) for item in leads), key=lambda item: item["score"], reverse=True)
