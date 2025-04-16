Git Workflow Checklist for VS Code

🔄 Before You Start Coding (Optional but Good Habit)
Open Terminal in VS Code
git pull --no-rebase

This ensures you have the latest version from GitHub before you start working.
📝 While You Work
Make changes to your files.
Save often (Cmd+S or Ctrl+S).

💾 After You Finish a Session (Commit + Push)
1️⃣ Stage your changes
bash
git add .
git commit -m "describe what you did"
git push

🔄 When Switching Devices (or Collaborating)
If you work on this repo from another device, always pull first:
bash
git pull --no-rebase

🚨 If Git Refuses to Pull (Conflicts or Divergence)
Check if you have uncommitted changes.
Either:
Commit your changes.
Or stash your changes:bashCopyEditgit stash

Then try:bash
git pull --no-rebase

If you stashed changes, bring them back
bash: git stash pop
