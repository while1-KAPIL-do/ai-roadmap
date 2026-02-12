# Prompt Engineering – Master Cheat Sheet

Reusable instruction blocks used by AI engineers in real production systems.

Goal:
Write predictable, safe, machine-friendly prompts FAST.

---

---

# 🧠 Core Formula

Most professional prompts follow:

TASK  
+ FORMAT  
+ RESTRICTIONS  
+ FALLBACK  

---

---

# 🟢 TASK VERBS (What AI must do)

Use these to define the job.

- Summarize  
- Extract  
- Classify  
- Assess  
- Explain  
- Write  
- Provide  
- Answer  
- Generate  
- Rewrite  
- Translate  
- List  
- Identify  
- Compare  

---

---

# 🟡 FORMAT CONTROL (How output should look)

These shape the response.

- Return only  
- Return exactly  
- Return as bullet points  
- Return a numbered list  
- Maximum X lines  
- Maximum X sentences  
- One word answer  
- Short response  
- Table format  
- Key-value pairs  

---

---

# 🟡 JSON ENFORCEMENT (Very Common)

Return ONLY valid JSON:
{
  "field": ""
}

Do not include extra text.

---

---

# 🔵 VOCABULARY CONTROL (Prevent creativity)

Used heavily in enterprise.

- Allowed values:  
- Choose one of:  
- Use only:  
- Select from:  

Example:
Allowed values: low, medium, high.

---

---

# 🟣 SAFETY / ANTI-HALLUCINATION

Critical for reliability.

- If missing → "unknown"  
- If not found → "not present"  
- If unclear → "unknown"  
- If information is insufficient → "unknown"  
- Do not guess  
- Do not fabricate  
- Use only provided text  

---

---

# 🟠 BEHAVIOR / STYLE CONTROL

Controls personality & tone.

- Professional  
- Friendly  
- Polite  
- Simple language  
- For beginners  
- Technical  
- Keep concise  
- No blame  
- No promises  

---

---

# 🟤 PRECISION ENFORCERS

Reduce randomness.

- Exactly  
- At most  
- No more than  
- Strictly  
- Only  

Example:
Return exactly 3 bullet points.

---

---

# 🔴 OUTPUT BOUNDARY

Prevents extra chatter.

- Do not include extra text  
- No commentary  
- Only return the result  
- Nothing outside the JSON  

---

---

# 🧠 FALLBACK PATTERNS

What happens when AI cannot answer.

- return "unknown"  
- return "other"  
- return "not present"  
- return insufficient_data  

---

---

# 🧠 PROFESSIONAL EXTRA RULES

Common in production prompts.

- Be deterministic  
- Prefer accuracy over creativity  
- If unsure, say unknown  
- Do not assume missing data  
- Follow the format strictly  

---

---

# 🧠 PROMPT SELF-CHECK (Senior Habit)

Before finalizing, ask:

- Did I define format?  
- Did I restrict vocabulary?  
- Did I handle missing info?  
- Did I forbid extra output?  

If any answer = no → improve.

---

---

# 🧠 BEGINNER vs ENGINEER

Beginner:
asks questions.

Engineer:
designs behavior.

---

---

# 🚀 MEMORY LINE

If software cannot read it → it is useless.

---

---

# 🎯 What Mastery of This Sheet Gives You

You will:

- build reliable AI features  
- reduce bugs  
- integrate faster  
- impress interviewers  
- think like product engineers  

---
