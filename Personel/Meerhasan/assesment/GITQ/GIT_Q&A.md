1) What is GIT?
Ans : Git (/ɡɪt/) is a version control system for tracking changes in computer files and coordinating work on those files among multiple people. It is primarily used for source code management in software development, but it can be used to keep track of changes in any set of files.

2) What is a repository in GIT?
Ans : Git is a program that tracks changes made to files. ... A Git repository is the . git/ folder inside a project. This repository tracks all changes made to files in your project, building a history over time.

3) What is the command you can use to write a commit message?
Ans : git commit -m “ “

4) What is the difference between GIT and SVN?
Ans : The difference between Git and SVN version control systems is that Git is a distributed version control system, whereas SVN is a centralized version control system. Git uses multiple repositories including a centralized repository and server, as well as some local repositories.

5) What are the advantages of using GIT?
Ans : 

6) What language is used in GIT?
Ans : Git uses ‘C’ language. GIT is fast, and ‘C’ language makes this possible by reducing the overhead of run times associated with high-level languages.

7) What is the function of ‘GIT PUSH’ in GIT?
Ans : The git push command allows you to send (or push) the commits from your local branch in your local Git repository to the remote repository.

8) Why GIT better than Subversion?
Ans : Git has the advantage that it's MUCH better suited if some developers are not always connected to the master repository. Also, it's much faster than SVN. And from what I hear, branching and merging support is a lot better



9) What is “Staging Area” or “Index” in GIT?
Ans : The Git index is used as a staging area between your working directory and your repository. You can use the index to build up a set of changes that you want to commit together. When you create a commit, what is committed is what is currently in the index, not what is in your working directory.

10) What is GIT stash?
Ans : Sometimes you want to switch the branches, but you are working on an incomplete part of your current project. You don't want to make a commit of half-done work. Git stashing allows you to do so. The git stash command enables you to switch branches without committing the current branch

11)  What is GIT stash drop?
Ans : In case we do not need a specific stash, we use git stash drop command to remove it from the list of stashes.

12) How will you know in GIT if a branch has been already merged into master?
Ans : To know if a branch has been merged into master or not you can use the below commands:
git branch --merged – It lists the branches that have been merged into the current branch.
git branch --no-merged – It lists the branches that have not been merged.

13) What is the function of git clone?
Ans : Git, cloning is the act of making a copy of any target repository. The target repository can be remote or local. You can clone your repository from the remote repository to create a local copy on your system. Also, you can sync between the two locations.

14) What is the function of ‘git config’?
Ans : The git config command is a convenience function that is used to set Git configuration values on a global or local project level. These configuration levels correspond to . gitconfig text files. Executing git config will modify a configuration text file.

15) What does commit object contain?
Ans : The commit object contains following information:
    • HASH: The SHA1 hash of the Git tree that refers to the state of index at commit time. 
    • Commit Author: The name of person/process doing the commit and date/time. 
    • Comment: Some text messages that contains the reason for the commit .


16) How can you create a repository in Git?
Ans : To create a repository, create a directory for the project if it does not exist, then run the command “git init”. By running this command .git directory will be created in the project directory.

17) What is ‘head’ in git and how many heads can be created in a repository?
Ans : A head is simply a reference to a commit object. In every repository, there is a default head referred as “Master”. A repository can contain any number of heads.

18) What is the purpose of branching in GIT
Ans : In Git, branches are a part of your everyday development process. Git branches are effectively a pointer to a snapshot of your changes. When you want to add a new feature or fix a bug—no matter how big or how small—you spawn a new branch to encapsulate your changes.

19) What is the common branching pattern in GIT?’
Ans : branch and create another branch to implement new features. This pattern is particularly useful when there are multiple developers working on a single project.

20) How can you bring a new feature in the main branch?
Ans : We can use a command “git merge” or “git pull command”, to bring a new feature in the main branch.


21) What is a ‘conflict’ in git?
Ans : Git can handle on its own most merges by using its automatic merging features. There arises a conflict when two separate branches have made edits to the same line in a file, or when a file has been deleted in one branch but edited in the other. Conflicts are most likely to happen when working in a team environment.

22) How can conflict in git resolved?
Ans : To resolve the conflict in git, edit the files to fix the conflicting changes and then add the resolved files by running “git add” after that to commit the repaired merge,  run “git commit”.  Git remembers that you are in the middle of a merger, so it sets the parents of the commit correctly.

23) To delete a branch what is the command that is used?
Ans : If you are sure you want to delete it, run 'git branch -D my-branch'. This is the command to use if you want to permanently throw away all of the commits associated with a particular line of development.

24) What is another option for merging in git?
Ans : “Rebasing” is an alternative to merging in git.

25) What is GIT version control?
Ans : The version control system is a collection of software tools that help a team to manage changes in a source code. It uses a special kind of database to keep track of every modification to the code.

26) What is the function of ‘git diff ’ in git?
Ans : Diff command is used in git to track the difference between the changes made on a file. Since Git is a version control system, tracking changes are something very vital to it. Diff command takes two inputs and reflects the differences between them.

27) What is ‘git status’ is used for?
Ans : The git status command is used to display the state of the repository and staging area. It allows us to see the tracked, untracked files and changes. This command will not show any commit records or information. 


28) What is the difference between the ‘git diff ’and ‘git status’?
Ans : ‘git diff’ is similar to ‘git status’, but it shows the differences between various commits and also between the working directory and index.

29) What is the function of ‘git checkout’ in git?
Ans : It checks the branches and updates the files in the working directory to match the version already available in that branch, and it forwards the updates to Git to save all new commit in that branch.

30) What is the function of ‘git rm’?
Ans : To remove the file from the staging area and also off your disk ‘git rm’ is used.

31) What is the function of ‘git stash apply’?
Ans : When you want to continue working where you have left your work, ‘git stash apply’ command is used to bring back the saved changes onto the working directory.

32) What is the use of ‘git log’?
Ans : To find specific commits in your project history- by author, date, content or history ‘git log’ is used.

33) What is ‘git add’ is used for?
Ans : This command updates the current content of the working tree to the staging area. It also prepares the staged content for the next commit. Every time we add or update any file in our project, it is required to forward updates to the staging area. 

34) What is the function of ‘git reset’?
Ans : The function of ‘Git Reset’ is to reset your index as well as the working directory to the state of your last commit.

35) Explain what is commit message?
Ans : Commit message is a feature of git which appears when you commit a change. Git provides you a text editor where you can enter the modifications made in commits.


36) Name a few Git repository hosting services
ans : 
    • Visual Studio Online 
    • Pikacode 
    • GitHub 
    • GitEnterprise 
    • SourceForge.net 

