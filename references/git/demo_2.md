# Changing Git users on the repo level

1. Open the <repo>/.git/config file
2. Add the following code to the config file
```
[user]
    email = "<email_to_set_on_this_repo>"
```
3. You may need to enter an access token upon first commit with the new credentials