- [Setup](#setup)
- [Reset all files to specific commit, alters commit history](#reset-all-files-to-specific-commit-alters-commit-history)
- [Revert changes made in a specific commit, doesn't alter commit history](#revert-changes-made-in-a-specific-commit-doesnt-alter-commit-history)
- [Change most recent commit comment](#change-most-recent-commit-comment)

# Setup
1. if needed run 

```
git branch -D git_demo_1
```

2. set up branch and several commits
```
git checkout -b git_demo_1 && \
echo "hello world" > git_demo_1.txt && \
git add . && \
git commit -m 'commit 1' && \
echo "commit 2" >> git_demo_1.txt && \
git add . && \
git commit -m 'commit 2' && \ 
echo "commit 3" >> git_demo_1.txt && \
git add . && \
git commit -m 'commit 3' && \
echo "2nd file" > git_demo_1_2.txt && \
git add . && \
git commit -m 'commit 4'
```

# Reset all files to specific commit, alters commit history
```
git reset <commit hash>
```

# Revert changes made in a specific commit, doesn't alter commit history
```
git revert <commit hash>
```

# Change most recent commit comment
```
git commit -amend -m 'previous commit message amended'
```