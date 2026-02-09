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



