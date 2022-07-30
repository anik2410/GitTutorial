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
 # create a folder in the local directory
  # example: created a local repo at C:/Users/anik2/Documents/demorepolocal using powershell cmdlet:
  # New-Item -Path C:/Users/anik2/Documents/dmorepolocal -ItemType directory
# to add the folder to online GitHub repo go to GitHub and create an empty repo
# then on the VS termial type the following to initialize the Git Repo
git init
# after initializing we can create a README.md by the following
git add README.md
# we can commit the README.md to the local git by the following
git commit -m"add any text"
# create a main branch using the following
git branch -M main
# after initializing Git go to GitHub to the created new empty repo and copied the SSH keys
# add the following code to add the origin to the remote Git Repo
git remote add origin git@github.com:anik2410/demorepolocal.git
# to check the remote origin exist
git remote -v
# following code push the local repo to online repo
git push -u origin main
# the following lines are edited/added in the 'featurebranch-gitcommands'
# adding a branch
# to add a branch we need to create the branch first using git commands in our local repo
git branch
 # this will show the branch we have in our repo and will put an asteriks mark on the current used one
git checkout -b name of the branch
 # this command will create the branch we want to add as an example:
 # git checkout -b feature-branch
 # here feature-branch is created/ checked out
# now typing git branch will show that we are in the newly created branch 
# now if we want to commit the changes to this feautre branch then we add (stage) the changes and commit them
git add .
git commit -m "add description of the commit"
# now push the committed changes to the online repo
# this line is being added while in the featurebranch-gitcommands