# Technical Incident Report — Base Template
**Alijó IT Workshops | Standard Documentation Format**

> **Documentation Rule:** A statement such as *"it works now"* is not sufficient evidence. Every resolved incident must include verifiable command output, log excerpts, or screenshots.

---

## 1. Executive Summary
* **Workshop / Lab Name:** 
* **Team Name & Members:** 
* **Date:** 
* **Overall Status:** `[ ] All Resolved` | `[ ] Partially Resolved` | `[ ] Escalated`
* **Summary:** *(2–3 sentences summarizing the incidents handled and their final outcome).*

---

## 2. System Baseline Information
* **Hostname:** 
* **Operating System / Version:** 
* **Primary Network Interface & IPv4 Address:** 
* **Default Gateway & DNS Server(s):** 

---

## 3. Incident Breakdown *(Duplicate this section for each incident)*

### Incident ID & Title: 
* **Reported Symptoms:** *(What failed from the user's perspective?)*
* **Investigation & Evidence Collected:** *(Commands run and relevant output/logs before making changes).*
* **Hypothesis & Root Cause:** *(What actually caused the failure and how the evidence proved it).*
* **Resolution Applied:** *(Exact commands or configuration changes executed).*
* **Verification Tests:** *(Commands re-run after the fix proving service restoration and no side effects).*

---

## 4. Lessons Learned & Prevention
* **Key Takeaway:** *(What diagnostic step was most critical?)*
* **Future Prevention:** *(How could this misconfiguration or failure be prevented in a production environment?)*
