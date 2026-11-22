# Gemini Guide for IT Technicians & Students
**02-Artificial-Intelligence | Alijó IT Workshops**

---

## 1. Overview & Best Use Cases in IT Labs
Gemini is well suited for multimodal troubleshooting (analyzing terminal screenshots alongside text logs), synthesizing documentation across Linux man pages and networking RFCs, and structuring clear step-by-step diagnostic workflows.

### Recommended IT Lab Tasks
* Interpreting screenshots of network diagrams, Wireshark packet captures, or VM console errors when copy-pasting text is limited.
* Cross-referencing Linux command syntax (`ip`, `ss`, `ufw`, `systemctl`, `journalctl`) and explaining how specific flags interact.
* Generating structured comparison tables (e.g., comparing safe vs. unsafe remediation options) and verification checklists.
* Translating technical root-cause findings into concise, audience-ready incident reports.

---

## 2. Recommended Workflow in Workshops
1. **Combine Context + Raw Output:** State the Ubuntu environment, service goal, and exact terminal output (or attach a sanitized screenshot of the error).
2. **Enforce Verification-First Constraints:** Explicitly instruct Gemini to provide read-only diagnostic commands before any configuration or permission changes.
3. **Request Structured Output:** Ask for a compact table or numbered checklist separating *Hypothesis*, *Diagnostic Command*, and *Expected Healthy Output*.
4. **Audit Locally:** Run `man <command>` or `<command> --help` on your Ubuntu VM to confirm every flag before executing any command.

---

## 3. Strengths & Watch-Outs for IT Troubleshooting

| Strengths | Common Watch-Outs / Failure Modes |
| :--- | :--- |
| Handles mixed text logs, configuration blocks, and error screenshots in a single prompt. | May offer multiple alternative solutions at once; ask it to prioritize the safest, least-invasive option first. |
| Clear at formatting structured troubleshooting matrices and post-incident reports. | Can generalize across Linux distributions (Debian/Ubuntu vs. RHEL/Fedora) unless `Ubuntu 24.04` is stated explicitly. |
| Helpful for explaining underlying TCP/IP, DNS, and Linux permission concepts alongside CLI steps. | Requires human verification of paths, interface names (`ens33`, `eth0`), and service units on the local VM. |

---

## 4. Quick Prompt Template for Gemini

```text
Environment: Ubuntu 24.04 LTS Desktop VM (Lab Sandbox)
Goal: Diagnose and verify the root cause of [describe issue] without making blind changes.

Evidence:
[Paste sanitized log lines, CLI output, or script snippet]

Instructions:
1. Analyze the exact error message and list the top 2 probable causes.
2. Provide a table with: Probable Cause | Read-Only Verification Command | Expected Output if Confirmed.
3. Explain all command flags and respect least-privilege security (no chmod 777, no disabling UFW).
```
