# Git Commit Message Rules & Examples

A quick reference for writing clean, professional, industry-standard commits.

---

# 🎯 Purpose of a Commit
A commit should clearly explain:

1. What changed  
2. Why it changed (if necessary)

Someone reading history months later should understand the project evolution.

---

---

# 🧠 Golden Format
<verb> + <what> + <optional context>


Examples:
- Add API timeout handling
- Fix null response parsing
- Refactor monitoring flow

---

---

# 🟢 Standard Verbs (Use These)

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

---

# 🟢 20 GOOD COMMIT EXAMPLES

### Features
1. Add API health check logic  
2. Add response time measurement  
3. Implement retry mechanism for failures  
4. Create monitoring service module  

### Fixes
5. Fix crash when API returns empty body  
6. Fix incorrect error status mapping  
7. Fix missing null check for address  
8. Fix JSON parsing for nested fields  

### Improvements
9. Improve console output readability  
10. Improve error message formatting  
11. Optimize request execution  
12. Improve logging structure  

### Refactor
13. Refactor API calls into helper functions  
14. Refactor payload builder  
15. Refactor main flow for clarity  

### Safety / Validation
16. Handle missing user data safely  
17. Validate payload before POST request  

### Maintenance
18. Remove unused import  
19. Rename function for better clarity  

### Documentation
20. Add setup instructions in README  

---

---

# 🔴 20 BAD COMMIT EXAMPLES (NEVER DO)

1. update  
2. fix  
3. done  
4. changes  
5. work  
6. final  
7. test  
8. again  
9. ok  
10. wip  
11. misc  
12. try  
13. small change  
14. modify  
15. latest  
16. new  
17. corrected  
18. solved  
19. bug fix  
20. improvement  

Why bad?
Because they give **zero information**.

---

---

# ⚠️ Multiple Changes in One Commit

❌ Bad:
Fix API + refactor + formatting

✅ Better:
Fix API timeout handling
Refactor API helper structure
Format code for readability


One commit = one idea.

---

---

# 🧠 Length Rule

Short & precise.

✅ Add retry logic for network failures  
❌ Added a lot of retry logic for different network problems in many scenarios

---

---

# 🧠 Tense Rule

Use present tense.

✅ Add login validation  
❌ Added login validation  

---

---

# 🧠 Self Check Before Commit

Ask:
- Can someone understand this later?
- Is it specific?
- Is it one change?

If yes → commit.

---

---

# 🧠 What Recruiters Look For

They scan commit history for:
- clarity  
- structured progress  
- small incremental improvements  
- engineering communication  

Good commits build trust.

---

---

# 🧠 Example of Beautiful History

Add project base structure
Implement API request helper
Add error handling for failed requests
Refactor response formatter
Improve monitoring report readability
Add README with setup steps



This tells a story of growth.

---

---

# 🚀 Final Rule

Bad code can be fixed.  
Bad Git history stays forever.



# ################ Very Important ################# #

🧠 How Senior Engineers PLAN COMMITS BEFORE CODING

They think in:
steps of value delivery
Each commit should represent:
one idea
one improvement
one reversible step

🎯 Why plan commits first?

Because later someone should be able to:

✅ review it
✅ revert it
✅ understand it
✅ debug when it broke



🧩 Example — YOU building API Monitor

Let’s say feature is:
“Add API monitoring with response time”

❌ Beginner approach

Write everything → huge commit:
Add API monitor


# Inside:
new files
new logic
refactor
prints
error handling

-- Impossible to review.

✅ Senior approach (planned)

Before coding, they think:
Step 1
Create project skeleton.

Step 2
Add basic GET call.

Step 3
Add error handling.

Step 4
Add response timing.

Step 5
Improve output.

Step 6
Refactor helpers.

-- Now they code accordingly.

🧠 What Git history becomes
Add project base structure
Implement API GET request
Handle request exceptions
Add response time calculation
Improve report formatting
Refactor API helpers


# 🔥 This looks like craftsmanship.

🧠 Rule Seniors Follow

If I had to delete this commit,
would the system still make sense?

If YES → good commit.
If NO → commit too big.

🧠 Another Senior Trick

They keep commits:

Small enough to review
Big enough to matter

Tiny bad:

fix typo


Huge bad:

entire system rewrite

🧠 Planning commits = planning architecture

Because you are deciding:

boundaries

responsibilities

progression

This is product thinking.

🧩 How to apply this DAILY (very practical)

Before coding, write in notepad:

[ ] Add base structure
[ ] Add API caller
[ ] Add error handling
[ ] Add timing
[ ] Clean output


Each checkbox = future commit.

Now build.

🧠 What happens magically

You will:

Write cleaner code

Avoid mixing concerns

Think modular

Avoid chaos

Feel in control

🧠 Why recruiters love this

Because they see:

👉 structured evolution
👉 logical thinking
👉 maintainability mindset

Not random hacking.

🧠 Ultra Pro Level Thought

Great engineers can:

👉 understand a system
👉 by reading commit history

without reading code.


# sample commits for current project -

Add project base structure
Implement API GET helper
Handle request failures
Add response time measurement
Create API monitoring workflow
Improve report readability
Add documentation


# ############ MY PAST MISTAKES #############

# 🧠 Why commits use present tense

Git commit messages follow a convention:
Write the message as if it completes this sentence:
If applied, this commit will...

✅ Example
If applied, this commit will ADD API retry logic.
-- sounds correct.

❌ If you wrote past tense
If applied, this commit will ADDED API retry logic.
-- grammatically wrong.

# Always start with:

Add
Fix
Update
Remove
Refactor
Improve

-- Never:

Added
Fixed
Updated
Removed