# Git Daily Workflow – Sync, Update & Cleanup

How professional engineers keep their work aligned with the team and maintain a clean repository.

---

# 🎯 Goal

By following this guide, you will know how to:

- start from the latest code  
- keep your branch updated  
- reduce surprises in PR  
- clean finished branches  
- work like a team-ready engineer  

---

---

# 🧠 Team Reality

While you are coding, others are merging.

If you don’t sync → conflicts & confusion.  
If you sync → smooth development.

---

---

# ================================
# STEP 1 — START DAY WITH FRESH MAIN
# ================================

Always begin with:

```bash
git checkout main
git pull origin main
```

Now your main branch matches the remote.

Why this is critical

New branches must start from:
👉 the latest stable version.

# ================================
# STEP 2 — CREATE BRANCH FROM MAIN
# ================================
```bash
git checkout -b feature-name
```

Now your work is isolated and safe.

# ================================
# STEP 3 — MAIN CHANGED WHILE YOU WORKED
# ================================

Very common situation.

Someone merged new updates while you were coding.

Your branch is now behind.

Update your branch

Stay in your feature branch:

```bash
git merge main
```

This brings the latest changes into your branch.

Possible Results

🟢 Auto merge → good.
🟡 Conflict → fix it. Normal engineering life.

Why do this BEFORE PR?

Because reviewers expect:
👉 branch built on latest main.

Otherwise they will ask you to update.

# ================================
# STEP 4 — AFTER PR IS MERGED
# ================================

The branch has completed its job.

Delete it.

Delete locally

```bash
git branch -d feature-name
```

Delete remote

```bash
git push origin --delete feature-name
```

Why professionals delete

Old branches:
- clutter
- confuse
- make navigation hard

Clean repos show discipline.

# ================================
# STEP 5 — SEE MERGED BRANCHES
# ================================

```bash
git branch --merged
```

Useful for cleanup.

# ================================
# GOLDEN DAILY LOOP
# ================================

Start work:

```bash
git checkout main
git pull
```

Create branch:

```bash
git checkout -b feature
```

During work:

```bash
git add .
git commit
```

Before PR:

```bash
git merge main
```

After merge:

```bash
delete branch
```

Repeat forever.

## 🧠 What This Shows Professionally

You understand:
- freshness
- collaboration
- lifecycle
- hygiene

This is how teams expect engineers to operate.

## 🧠 Junior vs Strong Engineer

- Junior → many stale branches
- Strong → minimal, updated, clean

🚀 Final Rule

Always build from the latest main.