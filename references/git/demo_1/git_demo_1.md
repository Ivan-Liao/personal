- [setup](#setup)

# setup
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
git commit -m 'commit 3'
```