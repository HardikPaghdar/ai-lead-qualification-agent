import unittest
from app import qualify_lead, qualify_many

class QualificationTests(unittest.TestCase):
    def test_priority_lead(self):
        result = qualify_lead({"name":"Asha","company":"Northstar","role":"COO","need":"Automate manual customer onboarding and reporting","budget_usd":15000,"timeline_days":14,"company_size":80})
        self.assertEqual(result["tier"], "priority")
        self.assertGreaterEqual(result["score"], 70)
    def test_low_fit_lead_needs_nurture(self):
        result = qualify_lead({"name":"Sam","company":"Solo","role":"Founder","need":"website","budget_usd":500,"timeline_days":180,"company_size":1})
        self.assertEqual(result["tier"], "nurture")
    def test_sorting(self):
        leads = [{"name":"Low","company":"A","role":"x","need":"small","budget_usd":500,"timeline_days":180,"company_size":1},
                 {"name":"High","company":"B","role":"x","need":"Automate onboarding and reporting workflow","budget_usd":12000,"timeline_days":10,"company_size":60}]
        self.assertEqual(qualify_many(leads)[0]["lead"]["name"], "High")

if __name__ == "__main__": unittest.main()
