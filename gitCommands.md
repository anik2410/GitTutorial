# the first command to clone a repo to the local drive
git clone

# shows the status of the repo (list any changes/added/discarded/un added fils or folders)
git status

# only adds the created new file(s)
git add file name

# only adds the created new folder(s)
git add folder name

# adds any modified file or folder to the stage list before committing to the repo
git add .

# following command is to commit the changes to the local repository
git commit -m"Add the Message header" -m"Add a description to the message"
 # this 1st -m"" adds the name/heading of the message and the 2nd -m"" adds the description
 # this is required to write soemthing so that the changes can be tracked
 # this 'git commit' command only make changes to the local repo but does not add the cahnges to the GitHub

# following command is to push the changes to the online repo GitHUb granted that the Online repo existed
git push origin main
 # origin is the origin of the local folder 
 # main is the branch we want to push in the GitHub repository

# what if the onlie repo does not exist!
 # 