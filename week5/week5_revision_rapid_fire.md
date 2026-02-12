# Week 5 – Prompt Engineering Revision
# Rapid Fire Practice (Improved Engineer Versions)

This file contains upgraded, production-quality prompts from the rapid fire exercises.

Goal:
- clarity  
- safety  
- structured thinking  
- backend usability  

---

---

# Q1 – Summary Control

Summarize the text.

Use at most 2 lines.  
Keep the language simple.

If the content is missing or irrelevant, return "unknown".

---

---

# Q2 – Ticket Tagging

Classify the ticket into one of the following categories:
billing, tech, account, other.

Return only the category name.

If it does not fit, return "other".

---

---

# Q3 – Customer Reply

Reply to the customer.

Keep the response short and professional.  
Do not make promises or commitments.

---

---

# Q4 – Data Extraction

Extract the following details.

Return ONLY valid JSON:
{
  "name": "",
  "phone": ""
}

If any value is missing, use "unknown".  
Do not include extra text.

---

---

# Q5 – Risk Assessment

Assess the risk.

Return ONLY valid JSON:
{
  "risk": "yes/no",
  "confidence": "low/medium/high"
}

If the information is insufficient, return:
risk = "no", confidence = "low".

Do not include extra text.

---

---

# Q6 – Team Routing

Determine which team should handle this issue.

Allowed values:
infra, backend, frontend, security.

Return only the team name.  
If unclear, return "unknown".

---

---

# Q7 – Error Explanation

Explain the error to a junior developer.

Return exactly 3 bullet points.  
Keep the explanation concise.

---

---

# Q8 – Email Writing

Write an email body.

Include an apology.  
Do not assign blame.  
Maximum 4 lines.

---

---

# Q9 – Action Steps

Provide recommended actions.

Return a numbered list.  
Maximum 3 steps.  
Keep them practical.

---

---

# Q10 – Anti-Hallucination

Answer the question using only the provided information.

If the answer is not available, say "unknown".  
Do not guess or fabricate.

---

---

# Q11 – Person Information (from earlier practice)

Extract person information from the text.

Return ONLY valid JSON with keys:
name, job, city.

If any value is missing, use "unknown".  
Do not include extra text.

---

---

# Q12 – Email Importance

Determine if the email is important.

Return ONLY valid JSON in this format:
{
  "important": true/false,
  "reason": ""
}

Do not include anything outside the JSON.

---

---

# Q13 – Priority Classification (Few-Shot Style)

Classify the priority of the message.

Use only one of these values:
low, mid, high, highest.

Message: database down  
Priority: high

Message: cyber attack  
Priority: highest

Message: API slowness  
Priority: mid

Message: API is failing  
Priority:

---

---

# Q14 – Urgency Detection

Determine if the situation is urgent.

Return ONLY valid JSON in this format:
{
  "urgent": true/false,
  "reason": ""
}

If information is insufficient, set both values to "unknown".  
Do not include extra text.

---

---

# Q15 – General Safety Rule

If information is not available, say "unknown".  
Do not guess.

---

---

# 🧠 What This File Trains

By practicing these, you build:

- precision  
- constraint design  
- predictable outputs  
- production reliability  

This is real AI engineering thinking.

---

# 🚀 Memory Line

If software cannot read it → it is useless.
