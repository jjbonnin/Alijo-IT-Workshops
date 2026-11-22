# Claude Guide for IT Technicians & Students
**02-Artificial-Intelligence | Alijó IT Workshops**

---

## 1. Overview & Best Use Cases in IT Labs
Claude excels at deep log correlation, step-by-step root cause reasoning, reviewing multi-file configuration snippets, and auditing scripts for subtle edge cases and security flaws.

### Recommended IT Lab Tasks
* Analyzing long, noisy `journalctl`, firewall, or web server logs to separate symptoms from the underlying root cause.
* Auditing shell scripts, Python automation tools, or Nginx/Apache virtual host configs for logic errors and security risks.
* Designing structured incident response plans and post-mortem documentation.
* Comparing two configuration files or terminal outputs to spot subtle discrepancies.

---

## 2. Recommended Workflow in Workshops
1. **Provide Clean, Unedited Logs:** Paste exact, sanitized error blocks rather than paraphrasing what happened.
2. **Separate Context from Evidence:** Use clear labels or XML-style tags (`<environment>`, `<logs>`, `<constraints>`) so Claude cleanly distinguishes your system setup from raw terminal output.
3. **Ask for Ranked Hypotheses:** Request the top 2–3 most likely root causes ordered by probability, along with a single non-destructive command to confirm or rule out each one.
4. **Verify Before Applying:** Validate every proposed command with `man <command>` or `--help` inside your Ubuntu VM before execution.

---

## 3. Strengths & Watch-Outs for IT Troubleshooting

| Strengths | Common Watch-Outs / Failure Modes |
| :--- | :--- |
| Strong at tracing multi-step causal chains across logs and code. | Can produce verbose explanations when you only need a concise CLI verification step unless told to be brief. |
| Good at spotting subtle logic inversions (e.g., exit codes, inverted percentages) in scripts. | May over-engineer simple one-line fixes into complex wrapper scripts if constraints are not specified. |
| Reliable at following strict negative constraints (*"do not modify permissions"*). | Like all LLMs, has no live visibility into your local VM state until you paste the command output. |

---

## 4. Quick Prompt Template for Claude

```text
<environment>
OS: Ubuntu 24.04 LTS (Lab VM)
Service / Component: [e.g., nginx / systemd / Python diagnostic script]
</environment>

<evidence>
[Paste exact sanitized terminal output, log lines, or script code]
</evidence>

<task>
1. Identify the 2 most likely root causes based strictly on the evidence above.
2. Provide one read-only verification command for each hypothesis and explain its flags.
3. Wait for my verification output before proposing configuration changes.
</task>
```
