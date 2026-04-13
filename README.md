# Prompt Engineering Playbook

A practical, example-driven playbook to learn and apply prompting techniques for day-to-day work (coding, analysis, writing, planning, troubleshooting). This repo is organized as a set of technique folders with simple templates and examples you can copy/paste and adapt. [1](https://github.com/prasantmohanty/prompt-engineering-playbook)

---

## 📂 Repository Structure

- **01 Role Based Prompting/**
- **02 Chain of Thought/**
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

### 1) Persona / Context Setting

#### ✅ Role Based Prompting (`01 Role Based Prompting`)
**What it helps with (2–3 lines):**  
Role-based prompting improves output quality by setting a **clear persona** (e.g., “Senior Java architect”, “QA lead”, “Security reviewer”). This reduces ambiguity and aligns tone, depth, and decision-making style with the role you need. [1](https://github.com/prasantmohanty/prompt-engineering-playbook)[2](https://www.promptingguide.ai/techniques)

**Best for:** code reviews, architecture guidance, troubleshooting, writing in a specific style.

**Template:**
```text
Act as a <ROLE>. 
Context: <BACKGROUND / DOMAIN / SYSTEM>.
Task: <WHAT YOU WANT>.
Constraints: <RULES / DOs & DON’Ts>.
Output format: <BULLETS / TABLE / JSON / STEPS>.