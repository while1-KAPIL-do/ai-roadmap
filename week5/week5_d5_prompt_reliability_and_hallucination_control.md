# Week 5 – Day 5  
# Prompt Reliability & Hallucination Control

---

## 🎯 Goal
Make AI outputs:

- safer  
- more truthful  
- more predictable  
- less creative when creativity is not desired  

This is critical for real-world systems.

---

---

## 🧠 First Understand the Problem

AI sometimes:

- guesses  
- invents  
- sounds confident but wrong  

Why?

Because the model's goal is to produce an answer, not to guarantee truth.

---

---

## 🧠 Example of Hallucination

Question:
Who is the CEO of Mars colony?

AI might invent a person.

Because it prefers answering over admitting uncertainty.

---

---

## 🧠 Why This Is Dangerous in Products

In real applications:

- wrong data → wrong automation  
- wrong automation → business damage  

So engineers must control this behavior.

---

---

## 🧠 Key Principle

Reduce guessing.  
Increase honesty.

---

---

## 🧠 Method 1 — Allow the Model to Say "I Don't Know"

One of the most effective techniques.

Example instruction:

If information is not available, say "unknown".  
Do not guess.

This alone can dramatically improve reliability.

---

---

## 🧠 Method 2 — Limit the Source of Truth

Example:

Answer ONLY from the provided text.  
If not found, say "not present".

Now hallucinations drop sharply.

---

---

## 🧠 Method 3 — Force Evidence

Example:

Provide the answer and quote the supporting line.

If the model cannot find proof, it becomes cautious.

---

---

## 🧠 Method 4 — Reduce Open Freedom

Bad:
Explain the company.

Better:
List 3 facts about the company from the text.

Boundaries improve safety.

---

---

## 🧠 Method 5 — Use Structured Output

Structured responses reduce randomness and unnecessary creativity.

---

---

## 🧠 Method 6 — Provide a Fallback

Example:

If unsure, return:

{
  "status": "insufficient_data"
}

Systems love predictable fallbacks.

---

---

## 🧠 What Professionals Aim For

They want AI to be:

- boring  
- safe  
- repeatable  

Not dramatic.

---

---

## 🧠 Real Industry Truth

The best AI systems are not flashy.

They are dependable.

---

---

## 🧠 Golden Memory Line

Correct and safe is better than smart sounding.

---

---

## 🧪 Practice Exercise 1

Original dangerous prompt:
Who will win the election?

Improve it by adding:
- avoid prediction  
- state uncertainty  
- no guessing  

---

---

## 🧪 Practice Exercise 2

Original:
Summarize the document.

Improve it by adding:
- only use provided text  
- if not present, say unknown  

---

---

## 🧠 Beginner vs Engineer

Beginner:
likes creative answers.

Engineer:
needs controlled answers.

---

---

## 🧠 What You Achieved This Week

You now understand how to:

- control outputs  
- design system behavior  
- use examples  
- structure responses  
- reduce hallucinations  

This is the thinking foundation behind AI products.

---

---

## ✅ Week Complete When You Understand

✔ AI must be guided  
✔ safety is more important than creativity  
✔ constraints improve quality  

---