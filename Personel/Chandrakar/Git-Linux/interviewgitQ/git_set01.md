


1)      What is GIT?
Ans . Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.




2)      What is a repository in GIT? 
Ans .Git is a program that tracks changes made to files. ... A Git repository is the . git/ folder inside a project. This repository tracks all changes made to files in your project, building a history over time





3)      What is the command you can use to write a commit message?
Ans . Use on commit  -m “enter you comments ”.




4)      What is the difference between GIT and SVN?
Ans. The difference between Git and SVN version control systems is that Git is a distributed version control system, whereas SVN is a centralized version control system. Git uses multiple repositories including a centralized repository and server, as well as some local repositories



5)      What are the advantages of using GIT?
Ans - Performance — Git is a strong and reliable platform in comparison with other versions of the control system
Security — The main purpose of Git is to manage the integrity of source code Quality Open Source Project — As earlier mentioned that Git is an open source project by having almost 10 years of operational history.



6)      What language is used in GIT?
Ans .  	C, Perl, Tcl, Python, C++



7)      What is the function of ‘GIT PUSH’ in GIT?
Ans - The git push command is used to upload local repository content to a remote repository.



8)      Why GIT better than Subversion?
Ans. Git has the advantage that it's MUCH better suited if some developers are not always connected to the master repository. Also, it's much faster than SVN.



9)      What is “Staging Area” or “Index” in GIT?
Ans. The Git index is a staging area between the working directory and repository. It is used to build up a set of changes that you want to commit together.



10)   What is GIT stash?
Ans. The git stash command takes your uncommitted changes (both staged and unstaged), saves them away for later use, and then reverts them from your working copy.


11)   What is GIT stash drop?
Ans . Dropping a stash will change the stash@{n} designations of all stashes further down the stack.


12)   How will you know in GIT if a branch has been already merged into master?
Ans . Run command git merge-base <commit-hash-step1> <commit-hash-step2> . If output of step 3 is same as output of step 2, then a "branch" has been already merged into master.



13)   What is the function of git clone?
Ans -Clones a repository into a newly created directory, creates remote-tracking branches for each branch in the cloned repository



14)   What is the function of ‘git config’?
Ans.The git config command is a convenience function that is used to set Git configuration values on a global or local project level. These configuration levels correspond to . gitconfig text files. Executing git config will modify a configuration text file



15)   What does commit object contain?
Ans. The commit object contains the directory tree object hash, parent commit hash, author, committer, date and message.



16)   How can you create a repository in Git?
Ans.Start a new git repository
    1. Create a directory to contain the project.
    2. Go into the new directory.
    3. Type git init .
    4. Write some code.
    5. Type git add to add the files (see the typical use page).
    6. Type git commit



17)   What is ‘head’ in git and how many heads can be created in a repository?
Ans - A repository can contain any number of heads. When you checkout to any branch the HEAD revision changes to the latest commit of the new branch. We directly will not create head but when we commit, git creates a reference to that commit known as head.



18)   What is the purpose of branching in GIT?
Ans . In Git, branches are a part of your everyday development process. Git branches are effectively a pointer to a snapshot of your changes. When you want to add a new feature or fix a bug—no matter how big or how small—you spawn a new branch to encapsulate your changes.



19)  
Ans . But in Git it's common to create, work on, merge, and delete branches several times a day. You saw this in the last section with the iss53 and hotfix branches you created. You did a few commits on them and deleted them directly after merging them into your main branch.




20)   How can you bring a new feature in the main branch?
Ans . First, you need to make sure your local master is synchronized with the upstream master . Then, you merge the feature branch into master and push the updated master back to the central repository. Pull requests can be facilitated by product repository management solutions like Bitbucket Cloud or Bitbucket Server.




21)   What is a ‘conflict’ in git?
Ans.Git can handle most merges on its own with automatic merging features. A conflict arises when two separate branches have made edits to the same line in a file, or when a file has been deleted in one branch but edited in the other. Conflicts will most likely happen when working in a team environment



22)   How can conflict in git resolved?
Ans. The easiest way to resolve a conflicted file is to open it and make any necessary changes.
    1. After editing the file, we can use the git add a command to stage the new merged content.
    2. The final step is to create a new commit with the help of the git commit command.
    3. Git will create a new merge commit to finalize the merge.




23)   To delete a branch what is the command that is used?
Ans. Delete a branch with git branch -d <branch> . The -d option will delete the branch only if it has already been pushed and merged with the remote branch. Use -D instead if you want to force the branch to be deleted, even if it hasn't been pushed or merged yet. The branch is now deleted locally



24)   What is another option for merging in git?
Ans.First we run git checkout master to change the active branch back to master. Then we run the command git merge new-branch to merge the new feature into the master branch. Note that git merge merges the specified branch into the currently active branch.



25)   What is GIT version control?
Ans. Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. For the examples in this book, you will use software source code as the files being version controlled, though in reality you can do this with nearly any type of file on a computer



26)    What is the function of ‘git diff ’ in git?
Ans.Diff command is used in git to track the difference between the changes made on a file. Since Git is a version control system, 
tracking changes are something very vital to it. Diff command takes two inputs and reflects the differences between them



27)     What is ‘git status’ is used for?
Ans.The git status command displays the state of the working directory and the staging area


28)   What is the difference between the ‘git diff ’and ‘git status’?
Ans. git status command will display the whole current status of your working tree (files that are staged, modified, deleted, untracked etc.) ... For example, if you do git status -s , you will get all the differences from your working directory against your HEAD and your index including untracked files



29) What is the function of ‘git checkout’ in git?
Ans.checkout is getting changes out from the local or remote repository (into your local working directory).



30) What is the function of ‘git rm’?
Ans.The git rm command can be used to remove individual files or a collection of files. The primary function of git rm is to remove tracked files from the Git index. Additionally, git rm can be used to remove files from both the staging index and the working directory.


31)   What is the function of ‘git stash apply’?
Ans.git stash apply //apply the changes without removing stored files from stash area


32)   What is the use of ‘git log’?
Ans.Git log is a utility tool to review and read a history of everything that happens to a repository. Multiple options can be used with a git log to make history more specific. Generally, the git log is a record of commits



33)   What is ‘git add’ is used for?
Ans.git add. The git add command adds a change in the working directory to the staging area.



34) What is the function of ‘git reset’?
Ans.git reset is a powerful command that is used to undo local changes to the state of a Git repo. Git reset operates on "The Three Trees of Git". These trees are the Commit History ( HEAD ), the Staging Index, and the Working Directory.


35)   Explain what is commit message?

he commit command is used to save changes to a local repository after staging in Git



36)   Name a few Git repository hosting services

Ans. Option 1: GitHub. Seriously, this is a valid option. ...
    • Option 2: GitLab. GitLab is probably the leading contender when it comes to alternative code platforms. ...
    • Option 3: Bitbucket. Bitbucket has been around for many years. ...
    • Option 4: SourceForge. ...
    • Option 5: Roll your own. ...
    • Option 6: All of the above.

