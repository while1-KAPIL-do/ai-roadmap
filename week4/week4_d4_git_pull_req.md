# Pull Request (PR) Guide – Team Collaboration Workflow

Learn how professional teams move code from a feature branch into the main branch safely.

---

# 🎯 Goal of Pull Requests

A Pull Request (PR) is how you say:

"I made changes in my branch.  
Please review and merge them into main."

---

---

# 🧠 Why PRs Exist

PRs enable:

- Code review  
- Discussion  
- Quality improvement  
- Safe merging  
- Transparent history  

They are fundamental in professional software development.

---

---

# 🧠 Industry Rule

🚨 No direct commits to main.

All work should go through:

branch → PR → review → merge


---

---

# 🧩 Standard PR Workflow

main
↓
create branch
↓
work & commit
↓
push branch
↓
open pull request
↓
review & discuss
↓
merge into main


---

---

# 🧩 Step 1 — Create a Branch

```bash
git checkout -b improve-report-format
```
🧩 Step 2 — Work & Commit

Edit files, then:

```bash
git add .
git commit -m "Improve report header formatting"
```

🧩 Step 3 — Push Branch

```bash
git push -u origin improve-report-format
```

🧩 Step 4 — Open PR on GitHub

After pushing, GitHub will show:

```bash
Compare & pull request
```

Click it.
## 🧠 What to Write in a PR
Title
Short & clear.

Example:
```bash
Improve report header formatting
```

Description
Bullet points explaining changes.

Example:

```bash
- Enhance readability of console output
- Add clear section separators
```

## 🧠 What Reviewers Look For
They check:
- clarity
- scope
- risk
- maintainability

They are not hunting mistakes — they want safety.
🧩 Step 5 — Merge PR

After review → click:

```bash
Merge pull request
```

Now changes enter main.

---
## 🧠 What Happens After Merge

Usually:

- the branch is deleted
- main becomes the source of truth

## 🧠 PR vs Direct Push

Direct push:

```bash
I changed it.
```
PR:

```bash
Let’s review this change together.
```
Professional collaboration.
## 🧠 Mindset Shift

A PR is not asking for permission.
It is inviting improvement.

## 🧠 Why Recruiters Value PR Knowledge

It signals:
- teamwork readiness
- process awareness
- communication ability
- maturity

### 🧪 Practice Exercise

Do this yourself:

- Create branch
- Make small change
- Commit
- Push
- Open PR
- Merge

Even if you are both author & reviewer.

## 🚀 Final Rule

Main should always remain stable.
Branches are where change happens.