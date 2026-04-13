# Prompt Engineering Playbook

A practical, example-driven playbook to learn and apply prompting techniques for day-to-day work (coding, analysis, writing, planning, troubleshooting). This repo is organized as a set of technique folders with simple templates and examples you can copy/paste and adapt. [1](https://github.com/prasantmohanty/prompt-engineering-playbook)

---

## 📂 Repository Structure

- **01 Role Based Prompting/**
- **02 Chain of Thought/**
- **03 Few-Shot Learning/**
- **04 Iterative Refinement/**
- **05 System Prompt and Personas/**
- **06 Conversation Memory/**
- **07 Understanding Jailbreak Attacks/**
- **08 Prompt Chaining/**
- **09 Context Engineering/**
- **10 Tree of Throughts/** 
- **LICENSE**
- **README.md** [1](https://github.com/prasantmohanty/prompt-engineering-playbook)

---

## 🎯 Who is this for?

- Developers, QAs, analysts, and product folks who want **repeatable prompt patterns**
- Teams adopting **AI assistants** and looking for **consistent outcomes**
- Anyone building a lightweight internal “prompt library” for common tasks

---

## ⚡ Quick Start (How to Use)

1. Pick a technique folder (e.g., `01 Role Based Prompting/`).
2. Copy a prompt template and replace placeholders (context, constraints, format).
3. Iterate: refine instructions, add examples, tighten output format.
4. Save your best prompt back into the relevant technique folder as a reusable snippet.

---

## 🧠 Prompting Techniques (Categorized)

| Technique | What it helps with | Best for |
|-------------------|---------|---------------|
| ✅ Role Based Prompting |  Role-based prompting improves output quality by setting a **clear persona** (e.g., “Senior Java architect”, “QA lead”, “Security reviewer”). This reduces ambiguity and aligns tone, depth, and decision-making style with the role you need. | code reviews, architecture guidance, troubleshooting, writing in a specific style. |
|✅ Chain of Thought (CoT) |CoT prompting helps with complex tasks by forcing a structured approach: clarify → break down → solve stepwise → verify.It improves reliability for debugging, planning, and multi-step decisions where a one-shot answer is often incomplete.|Debugging, root-cause analysis, incident triage Migration planning, architecture trade-offs, stepwise implementation plans Complex reasoning tasks (multi-constraint solutions)|
|✅ Few‑Shot Learning |Few‑shot prompting improves accuracy and consistency by embedding 2–5 examples (shots) in the prompt so the model learns the pattern in context without fine‑tuning. It’s especially effective when instructions alone are not enough and you need a specific output format, label space, or tone|Best for Classification (sentiment, priority, routing, risk labels) where consistent labels matter -Structured extraction (pulling fields into JSON, tables, schema) using consistent examples -Style/format control (write like an incident report, commit message style, test case format) by showing exemplars -Translation/rewrites/summarization when you want a very specific structure in the output|
|✅ Iterative Refinement|Iterative refinement improves output quality by progressively steering the model through feedback loops instead of expecting perfection in one prompt. It works by refining, critiquing, and correcting responses step by step, leading to higher accuracy, clarity, and alignment over multiple turns.|Best for -Complex or ambiguous tasks where requirements become clearer during exploration(design docs, migration plans, incident analysis) -High‑quality writing (executive summaries, PRDs, whitepapers, policies, blogs) -Code improvement (refactoring, performance tuning, securSity hardening) -Decision making where trade‑offs must be examined and optimized incrementally|
|✅ System Prompts and Personas |System prompts define global, non‑negotiable behavior rules for the model—what it must always do or never do. They are ideal for enforcing guardrails, tone, safety, output structure, and policy compliance across all interactions.|Enforcing security, legal, or compliance rules .Standardizing tone and behavior across teams or products . Preventing unwanted behaviors (hallucination, verbosity, unsafe output) . Defining “how the AI should behave by default”|
|✅ Conversation memory |Conversation memory helps the assistant retain key user preferences, context, and long‑running goals across interactions, so you don’t have to repeat yourself. It improves continuity, personalization, and consistency—especially for recurring workflows (enablement, reporting, mentoring, coaching, delivery planning).|Recurring workflows: weekly status reports, OKRs, enablement plans, training schedules .User preferences: tone, format (bullets, exec summary), tooling choices, coding standards.Long-term goals: learning roadmap, public writing goals, fitness/finance milestones. Project continuity: architecture decisions, constraints, team norms, definitions of done|
|✅ Understanding Jailbreak attacks |Understanding jailbreak attacks helps you design LLM apps that remain safe even when users (or external content) try to override system instructions, exfiltrate data, or trigger unsafe actions. Jailbreaks are closely related to prompt injection, where adversarial text changes the model’s behavior in unintended ways.|LLMs read instructions and data in the same channel (text), so attacker-controlled text can “compete” with your intended instructions.|
|✅ Prompt chaining|Prompt chaining breaks a complex task into a sequence of smaller, focused prompts, where each step builds on the previous output.|Complex tasks with clear intermediate steps .Workflows involving analysis → transformation → validation.High-stakes outputs where verification is required.Agentic or semi-automated workflows.Reducing hallucination by narrowing scope per step|
|✅ Context Engineering |Context engineering ensures the model receives the right information, at the right time, in the right structure to produce high‑quality outputs|Tasks depend on existing data, constraints, or history. Long prompts where signal can get lost in noise. RAG, dashboards, design reviews, policy interpretation.Multi‑step or agentic workflows.Enterprise use cases with domain‑specific inputs|
|✅ Tree of thoughts|Tree of Thoughts enables the model to explore multiple reasoning paths in parallel, compare alternatives, and converge on a better solution|Problems with multiple valid solution paths . Strategic planning and trade‑off analysis , Architecture or design decisions , Ambiguous or ill‑defined problems ,“What should we do?” or “Which option is best?” questions|

## 🤝 Contributing
Contributions welcome:

Add new technique folders with templates + examples
Keep guidance practical (copy/paste ready)
Add “When to use / When NOT to use” and pitfalls