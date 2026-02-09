# Git Playbook – Professional Development Workflow

A complete reference for writing commits, planning work, and using branches like engineers in real companies.

---

# 🎯 Why This Exists

Git history is not just storage.  
It is communication, documentation, and proof of engineering maturity.

Recruiters, teammates, and future you will read it.

---

---

# ================================
# PART 1 — COMMIT MESSAGE RULES
# ================================

## Golden Purpose
A commit should clearly explain:

- What changed
- Why (if necessary)

---

## Golden Format

<verb> + <what> + <optional context>


Examples:

Add API timeout handling
Fix null response parsing
Refactor monitoring flow


---

## Standard Verbs (Industry)

Add  
Fix  
Update  
Remove  
Refactor  
Improve  
Rename  
Move  
Document  
Test  
Configure  
Implement  
Handle  
Validate  
Optimize  
Create  
Initialize  

---

## Tense Rule

Use present tense.

✅ Add login validation  
❌ Added login validation  

Why?

Because commit is read as:

"If applied, this commit will **Add** login validation."

---

---

## Length Rule

Short & precise.

✅ Add retry logic for failed API requests  
❌ Added complex retry mechanism for handling different types of failures across modules

---

---

## One Commit = One Idea

If message needs "and" → split it.

❌

Fix API and refactor helpers


✅

Fix API timeout handling
Refactor API helper structure


---

---

## 20 GOOD EXAMPLES

1. Add API health check logic  
2. Implement GET request handler  
3. Handle request exceptions  
4. Add response time measurement  
5. Fix crash on empty response  
6. Fix incorrect status mapping  
7. Improve console output formatting  
8. Optimize request execution  
9. Refactor API logic into module  
10. Refactor payload builder  
11. Handle missing address safely  
12. Validate API payload  
13. Remove unused import  
14. Rename function for clarity  
15. Add README instructions  
16. Improve logging structure  
17. Configure request timeout  
18. Add default fallback values  
19. Move helpers to separate file  
20. Initialize monitoring workflow  

---

---

## 20 BAD EXAMPLES (Never Write)

update  
fix  
done  
changes  
work  
final  
test  
again  
ok  
wip  
misc  
try  
small change  
modify  
latest  
new  
corrected  
solved  
bug fix  
improvement  

These give ZERO context.

---

---

# ================================
# PART 2 — COMMIT MATURITY LEVELS
# ================================

Same change → different experience levels.

---

## Junior

fix api


---

## Early Mid

Add retry


---

## Mid

Add retry logic for failed API requests


---

## Senior

Add retry logic for transient API failures to improve reliability


---

## Staff+

Add retry logic for transient API failures to improve system reliability under network instability


---

## Lesson
Growth = better clarity, not bigger vocabulary.

---

---

# ================================
# PART 3 — HOW SENIORS PLAN COMMITS
# ================================

Juniors:
> Write code → commit later.

Seniors:
> Decide commits → write code accordingly.

---

## Example Plan

Before coding, write checklist:

[ ] Add project structure
[ ] Implement GET call
[ ] Handle errors
[ ] Add response timing
[ ] Improve output
[ ] Refactor helpers


Each item becomes a commit.

---

## Resulting History

Add project base structure
Implement API GET request
Handle request exceptions
Add response time calculation
Improve report formatting
Refactor API helpers


Beautiful, reviewable, professional.

---

---

## Senior Rule

If removing a commit breaks everything → commit is too big.

---

---

# ================================
# PART 4 — BRANCHING GUIDE
# ================================

## Purpose
Develop safely without breaking main.

---

## Industry Rule
🚨 Never work directly on main.

Main must remain:
- stable  
- deployable  
- trusted  

---

## Create Branch

git checkout -b add-retry-logic


---

## Work & Commit

git add .
git commit -m "Add retry logic for failed requests"


---

## Switch Back

git checkout main


Your change disappears (correct behavior).

---

## Merge

git merge add-retry-logic


Now main includes the feature.

---

---

## Daily Team Workflow

main → branch → work → commit → merge


Repeat forever.

---

---

## Good Branch Names

add-retry-logic  
fix-timeout  
improve-logging  
refactor-api-helper  

Bad:
test / temp / new / branch1

---

---

# ================================
# PART 5 — WHAT RECRUITERS SEE
# ================================

They often scan commit history in seconds.

Good history shows:
- small steps  
- intention  
- safety  
- growth  

Bad history shows chaos.

---

---

## Example of Impressive Timeline

Add project base structure
Implement API request helper
Handle request failures
Refactor response formatter
Improve monitoring report readability
Add README with setup steps


---

---

# 🚀 FINAL RULE

Bad code can be improved.  
Bad Git history is forever.