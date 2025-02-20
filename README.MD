step1: create a folder xyz
step2: to make a git hub repository  git init 
step3: git add <file name>
step4: git commit -m "xyz"
step5: git remote add origin <repository link>
step6: git branch
step6: git push origin main   check (code will push on your repository) 
  

...............................................................................
# Create a new branch
git branch <branch-name>

# List all branches
git branch

# Switch to a branch
git checkout <branch-name>

# Create and switch to a new branch
git checkout -b <branch-name>

# Delete a branch
git branch -d <branch-name>

# Push a branch to remote
git push origin <branch-name>

# Pull a branch from remote
git pull origin <branch-name>

# Merge a branch into the current branch
git merge <branch-name>

...........................................................................................
# Push all branches to remote
git push --all

# Push tags to remote
git push --tags

# Push a specific branch to remote
git push origin <branch-name>

# Force push a branch to remote
git push origin <branch-name> --force

.....................................................................................
