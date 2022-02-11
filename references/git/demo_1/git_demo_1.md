# setup
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

echo 1 && \
echo 2