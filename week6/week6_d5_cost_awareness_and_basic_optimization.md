# Cost Awareness & Basic Optimization

---

## 🎯 Goal Today

Understand:

- What tokens are  
- Why tokens matter  
- How prompts affect cost  
- How to reduce waste  

---

## 🧠 What is a Token?

A token is roughly:

- A word  
- Or part of a word  

Example:

"Explain APIs clearly"

= multiple tokens.

More text → more tokens → more cost.

---

## 🧠 Where Tokens Are Counted

You pay for:

- Input tokens (your prompt)  
- Output tokens (model response)  

Total cost = input + output

---

## 🧠 Why Engineers Must Care

If your app:

- Sends 2000 tokens  
- Gets 1000 token response  
- Runs 10,000 times per day  

You are burning money.

---

## 🧠 Biggest Token Waste Mistakes

❌ Long system prompts  
❌ Repeating instructions every time  
❌ Asking for verbose responses  
❌ Not limiting output length  

---

## 🧩 Optimization #1 — Keep Prompts Tight

Bad:

Please kindly explain in a very detailed manner...

Better:

Explain in 2 lines.

Less tokens.

---

## 🧩 Optimization #2 — Limit Output

Always specify:

Maximum 2 sentences.

or

Return only JSON.

Prevents long essays.

---

## 🧩 Optimization #3 — Reuse System Prompt

In production:

Instead of resending large system prompt every time,  
you maintain conversation state.

Less repetition → fewer tokens.

---

## 🧠 Optimization #4 — Don’t Over-Explain Format

Instead of:

Return JSON with fields name, email, phone number...

Use template:

```json
Return:
{
  "name": "",
  "email": "",
  "phone": ""
}
```

Cleaner. Shorter.

---

## 🧠 Optimization #5 — Truncate Inputs

If user sends 10,000 words:  
You don’t always need all.

Limit:

```python
input_text = input_text[:2000]
```

Engineers control context size.

---

## 🧠 Production Mindset Shift

Before:

Does it work?

Now:

Does it scale?

---

## 🧠 Hidden Interview Signal

If you say:

"I control output length to reduce token usage"

Interviewers see:  
Production awareness.

---

## 🧪 Exercise

Improve this prompt to reduce tokens:

You are a highly experienced backend software engineer with deep understanding of system design and distributed systems and now I want you to carefully analyze and thoroughly explain the below concept in a very detailed and comprehensive manner...

Make it efficient.

---

## 🧠 What You Completed in Week 6

You now know:

✔ How to call LLM  
✔ How to extract nested response  
✔ How to parse JSON  
✔ How to retry failures  
✔ How to think about cost  

You officially moved from:

Prompt thinker  

to  

AI backend integrator  

Huge milestone 👊

---