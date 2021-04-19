1)      What is GIT?
ans:
Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
**********************************************************************************************

2)      What is a repository in GIT?
ans:
In Git, the repository is like a data structure used by VCS to store metadata for a set of files and directories. It contains the collection of the files as well as the history of changes made to those files. Repository in Git is considered as your project folder. A repository has all the project-related data. Distinct projects have distinct repositories.
******************************************************************************************************************

3)      What is the command you can use to write a commit message?
ans:
The commit command is used to save changes to a local repository after staging in Git. However, before you can save changes in Git, you have to tell Git which changes you want to save as you might have made tons of edits. A great way to do that is by adding a commit message to identify your changes.

-m
This option sets the commit's message.

*********************************************************************************************************************************8

4)      What is the difference between GIT and SVN?
ans:
A)GIT:
1.Git is open source distributed vice control system developed by Linus Torvalds in 2005. It emphasis on speed and data integrity
2.Git has a Distributed Model.
3.In git every user has their own copy of code on their local like their own branch.
4.In git we do not required any Network to perform git operation. 
5.Git is more difficult to learn. It has more concepts and commands. 
6.Git deals with large number of files like binary files that change quickly that why it become slow.
7.In git we create only .git directory.
8.It does not not have good UI as compared to SVN.
9.Features of GIT:
Distributed System.
Branching.
Compatibility.
Non-linear Development.
Lightweight.
Open source.

B)SVN:
1.Apache Subversion is an open source software version and revision control system under Apache license.
2.SVN has a Centralized Model.
3.In SVN there is central repository has working copy that also make changes and committed in central repository.
4.In SVN we required Network for runs the SVN operation. 
5.SVN is much easier to learn as compared to git.
6.SVN control the large number of binary files easily.
7.In SVN we create .svn directory in each folder.
8.SVN has simple and better user interface .
9.Features of SVN:
Directories are versioned
Copying, deleting, and renaming.
Free-form versioned metadata .
Atomic commits.
Branching and tagging.
Merge tracking.
File locking.

*********************************************************************************************************************************

5)      What are the advantages of using GIT?
ANS:
One of the biggest advantages of Git is its branching capabilities. Unlike centralized version control systems, Git branches are cheap and easy to merge. This facilitates the feature branch workflow popular with many Git users. Feature branches provide an isolated environment for every change to your codebase
***********************************************************************************************************************************

6)      What language is used in GIT?
Ans:
C - 45% · Shell - 35% · Perl - 8% · Tcl - 5% · Python - 2% · C ++ - 2%.
*************************************************************************************************************************************

7)      What is the function of ‘GIT PUSH’ in GIT?
ans:
The git push command is used to upload local repository content to a remote repository. Pushing is how you transfer commits from your local repository to a remote repo. It's the counterpart to git fetch , but whereas fetching imports commits to local branches, pushing exports commits to remote branches.
****************************************************************************************************************************************

8)      Why GIT better than Subversion?
ans:
Git has the advantage that it's MUCH better suited if some developers are not always connected to the master repository. Also, it's much faster than SVN. And from what I hear, branching and merging support is a lot better 
****************************************************************************************************************

9)      What is “Staging Area” or “Index” in GIT?
ans:
The Git index is used as a staging area between your working directory and your repository. You can use the index to build up a set of changes that you want to commit together. When you create a commit, what is committed is what is currently in the index, not what is in your working directory.
***************************************************************************************************************************

10)   What is GIT stash?
ans:
The git stash command takes your uncommitted changes (both staged and unstaged), saves them away for later use, and then reverts them from your working copy.
****************************************************************************************************************************

11)   What is GIT stash drop?
ans:
Git stash is a temporary storage. When you're ready to continue where you left off, you can restore the saved state easily: git stash pop . Popping your stash removes the changes from your stash and reapplies the last saved state.
********************************************************************************************************************************************

12)   How will you know in GIT if a branch has been already merged into master?
ans:
git merge-base command to find the latest common commit between the two branches. If that commit is the same as your branch head, then the branch has been completely merged.
**********************************************************************************************************************************************

13)   What is the function of git clone?
ans:
Usage. git clone is primarily used to point to an existing repo and make a clone or copy of that repo at in a new directory, at another location. The original repository can be located on the local filesystem or on remote machine accessible supported protocols. The git clone command copies an existing Git repository.
*************************************************************************************************************************************

14)   What is the function of ‘git config’?
ans:
The git config command is a convenience function that is used to set Git configuration values on a global or local project level. These configuration levels correspond to . gitconfig text files. Executing git config will modify a configuration text file
***********************************************************************************************************************************************************
15)   What does commit object contain?
ans:
The commit object contains the directory tree object hash, parent commit hash, author, committer, date and message.
********************************************************************************************************************************************************

16)   How can you create a repository in Git?
ans:
Create a directory to contain the project.
Go into the new directory.
Type git init .
Write some code.
Type git add to add the files (see the typical use page).
Type git commit .
***********************************************************************************************************************

17)   What is ‘head’ in git and how many heads can be created in a repository?
ans:
A repository can contain any number of heads. When you checkout to any branch the HEAD revision changes to the latest commit of the new branch. We directly will not create head but when we commit, git creates a reference to that commit known as head.
***********************************************************************************************************************
18)   What is the purpose of branching in GIT?
ans:
In Git, branches are a part of your everyday development process. Git branches are effectively a pointer to a snapshot of your changes. When you want to add a new feature or fix a bug—no matter how big or how small—you spawn a new branch to encapsulate your changes.
***************************************************************************************************************************

19)   What is the common branching pattern in GIT?
ans:
 Git it's common to create, work on, merge, and delete branches several times a day. You saw this in the last section with the iss53 and hotfix branches you created. You did a few commits on them and deleted them directly after merging them into your main branch.
 *****************************************************************************************************************************

20)   How can you bring a new feature in the main branch?
ans:
First, you need to make sure your local master is synchronized with the upstream master . Then, you merge the feature branch into master and push the updated master back to the central repository. Pull requests can be facilitated by product repository management solutions like Bitbucket Cloud or Bitbucket Server.
***********************************************************************************************************************************

21)   What is a ‘conflict’ in git?
ans:
Git can handle most merges on its own with automatic merging features. A conflict arises when two separate branches have made edits to the same line in a file, or when a file has been deleted in one branch but edited in the other. Conflicts will most likely happen when working in a team environment.
**********************************************************************************************************************************

22)   How can conflict in git resolved?
ans:
The easiest way to resolve a conflicted file is to open it and make any necessary changes.
After editing the file, we can use the git add a command to stage the new merged content.
The final step is to create a new commit with the help of the git commit command.
Git will create a new merge commit to finalize the merge.
*******************************************************************************************************************************

23)   To delete a branch what is the command that is used?
ans:
If you are sure you want to delete it, run 'git branch -D my-branch'. This is the command to use if you want to permanently throw away all of the commits associated with a particular line of development.
*************************************************************************************************************************

24)   What is another option for merging in git?
ans:
Using git rebase Instead of git merge. Using the "git merge" command is probably the easiest way to integrate changes from one branch into another. However, it's not your only option: "git rebase" offers another, slightly different way of integration.
******************************************************************************************************************************************************************
25)   What is GIT version control?
ans:
Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. For the examples in this book, you will use software source code as the files being version controlled, though in reality you can do this with nearly any type of file on a computer.
**********************************************************************************************************************************

26)    What is the function of ‘git diff ’ in git?
ans:
Diffing is a function that takes two input data sets and outputs the changes between them. git diff is a multi-use Git command that when executed runs a diff function on Git data sources. These data sources can be commits, branches, files and more.
************************************************************************************************************************************************

27)     What is ‘git status’ is used for?
ans:
The git status command displays the state of the working directory and the staging area. It lets you see which changes have been staged, which haven't, and which files aren't being tracked by Git. Status output does not show you any information regarding the committed project history.
******************************************************************************************************************************************************

28)   What is the difference between the ‘git diff ’and ‘git status’?
ans:
 git status command will display the whole current status of your working tree 
 git diff:
 Git diff is a command-line utility. It's a multiuse Git command. When it is executed, it runs a diff function on Git data sources. These data sources can be files, branches, commits, and more. It is used to show changes between commits, commit, and working tree, etc.
 ********************************************************************************************************************************************************************************
29) What is the function of ‘git checkout’ in git?
ans:
The git checkout command lets you navigate between the branches created by git branch . Checking out a branch updates the files in the working directory to match the version stored in that branch, and it tells Git to record all new commits on that branch.
************************************************************************************************************************************************************************

30) What is the function of ‘git rm’?
ans:
The git rm command can be used to remove individual files or a collection of files. The primary function of git rm is to remove tracked files from the Git index. Additionally, git rm can be used to remove files from both the staging index and the working directory.
*******************************************************************************************************************************************************************

31)   What is the function of ‘git stash apply’?
ans:
git stash temporarily shelves (or stashes) changes you've made to your working copy so you can work on something else, and then come back and re-apply them later on.
*********************************************************************************************************************************************************

32)   What is the use of ‘git log’?
ans:
Git log is a utility tool to review and read a history of everything that happens to a repository. Multiple options can be used with a git log to make history more specific. Generally, the git log is a record of commits.
************************************************************************************************************************************************

33)   What is ‘git add’ is used for?
ans:
git add . adds all modified and new (untracked) files in the current directory and all subdirectories to the staging area (a.k.a. the index), thus preparing them to be included in the next git commit . Any files matching the patterns in the . gitignore file will be ignored by git add .
************************************************************************************************************************************************************

34) What is the function of ‘git reset’?
ans: 
To review, git reset is a powerful command that is used to undo local changes to the state of a Git repo. Git reset operates on "The Three Trees of Git". These trees are the Commit History ( HEAD ), the Staging Index, and the Working Directory.
****************************************************************************************************************************************************

35)   Explain what is commit message?
ans:
The commit command is used to save changes to a local repository after staging in Git. However, before you can save changes in Git, you have to tell Git which changes you want to save as you might have made tons of edits.
**********************************************************************************************************************

36)   Name a few Git repository hosting services
ans:
Option 1: GitHub. Seriously, this is a valid option. ...
Option 2: GitLab. GitLab is probably the leading contender when it comes to alternative code platforms. ...
Option 3: Bitbucket. Bitbucket has been around for many years. ...
Option 4: SourceForge. ...
Option 5: Roll your own. ...
Option 6: All of the above.

