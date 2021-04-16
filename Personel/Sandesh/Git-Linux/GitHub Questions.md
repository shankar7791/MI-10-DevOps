1. What is GIT?
Ans : GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

2. What is a repository in GIT?
Ans : A Git repository (or repo for short) contains all of the project files and the entire revision history. You'll take an ordinary folder of files (such as a website's root folder), and tell Git to make it a repository. This creates a . git subfolder, which contains all of the Git metadata for tracking changes.

3. What is the command you can use to write a commit message?
Ans : git commit -m

4. What is the difference between GIT and SVN?
ANs : The difference between Git and SVN version control systems is that Git is a distributed version control system, whereas SVN is a centralized version control system. Git uses multiple repositories including a centralized repository and server, as well as some local repositories.

5. What are the advantages of using GIT?

Ans : 
    Good distributed model as each developer gets a local repository with a full history of commits which makes git fast compared to other VCs.
    Branching capabilities and merging are easy (as they are cheap), good data integrity.
    They are free and open-source we can easily download the source code and performs changes to it. They can handle larger projects efficiently.
    The push/pull operations are faster with a simple They save time and developers can fetch and create pull requests without switching.
    Data redundancy and replications. Add ons can be written in many languages.
    They have good and faster network performance and superior disk utilization and they think about its data like a sequence of snapshots.
    The object model is very simple and minimizes push/pull data transfers.

6.  What language is used in GIT?
Ans : 	C, Perl, Tcl, Python, C++

7. What is the function of ‘GIT PUSH’ in GIT?
Ans : The git push command is used to upload local repository content to a remote repository. 

8. Why GIT better than Subversion?
Ans : Many people prefer Git for version control for a few reasons: It's faster to commit. Because you commit to the central repository more often in SVN, network traffic slows everyone down. Whereas with Git, you're working mostly on your local repository and only committing to the central repository every so often.
 
9. What is “Staging Area” or “Index” in GIT?
Ans : The staging area is like a rough draft space, it's where you can git add the version of a file or multiple files that you want to save in your next commit (in other words in the next version of your project).

10. What is GIT stash?
Ans : The git stash command takes your uncommitted changes (both staged and unstaged), saves them away for later use, and then reverts them from your working copy.

11. What is GIT stash drop?
Ans : The git stash drop command is used to delete a stash from the queue. Generally, it deletes the most recent stash. Caution should be taken before using stash drop command, as it is difficult to undo if once applied. The only way to revert it is if you do not close the terminal after deleting the stash. 

12. How will you know in GIT if a branch has been already merged into master?
Ans : We can use following commands for this purpose:

I. git branch --merged master : This prints the branches merged into master

II. git branch --merged lists : This prints the branches merged into HEAD (i.e. tip of current branch)

III. git branch --no-merged : This prints the branches that have not been merged

By default this applies only to local branches.

We can use -a flag to show both local and remote branches. Or we can use -r flag to show only the remote branches.

13. What is the function of git clone?
Ans : git clone is primarily used to point to an existing repo and make a clone or copy of that repo at in a new directory, at another location. The original repository can be located on the local filesystem or on remote machine accessible supported protocols. The git clone command copies an existing Git repository.

14. What is the function of ‘git config’?
Ans : The git config command is a convenience function that is used to set Git configuration values on a global or local project level. These configuration levels correspond to . gitconfig text files. Executing git config will modify a configuration text file.

15. What does commit object contain?
Ans : The commit object contains the directory tree object hash, parent commit hash, author, committer, date and message.

16. How can you create a repository in Git?
	Ans Create a directory to contain the project.
    Go into the new directory.
    Type git init .
    Write some code.
    Type git add to add the files (see the typical use page).
    Type git commit .
      
17. What is ‘head’ in git and how many heads can be created in a repository?
Ans : A repository can contain any number of heads. When you checkout to any branch the HEAD revision changes to the latest commit of the new branch. We directly will not create head but when we commit, git creates a reference to that commit known as head.
      
18. What is the purpose of branching in GIT?
Ans : In  Git, branches are a part of your everyday development process. Git branches are effectively a pointer to a snapshot of your changes. When you want to add a new feature or fix a bug—no matter how big or how small—you spawn a new branch to encapsulate your changes.

19. What is the common branching pattern in GIT?
Ans : Release Branches. Most software has a typical life cycle: code, test, release, repeat. 

20. How can you bring a new feature in the main branch?
Ans : First, you need to make sure your local master is synchronized with the upstream master . Then, you merge the feature branch into master and push the updated master back to the central repository. Pull requests can be facilitated by product repository management solutions like Bitbucket Cloud or Bitbucket Server.

21. What is a ‘conflict’ in git?
Ans : Git can handle most merges on its own with automatic merging features. A conflict arises when two separate branches have made edits to the same line in a file, or when a file has been deleted in one branch but edited in the other. Conflicts will most likely happen when working in a team environment.

22. How can conflict in git resolved?
Ans :The easiest way to resolve a conflicted file is to open it and make any necessary changes.
    After editing the file, we can use the git add a command to stage the new merged content.
    The final step is to create a new commit with the help of the git commit command.
    Git will create a new merge commit to finalize the merge.

23. To delete a branch what is the command that is used?
Ans : run 'git branch -D my-branch'. This is the command to use if you want to permanently throw away all of the commits associated with a particular line of development.

24. What is another option for merging in git?
Ans : Using the "git merge" command is probably the easiest way to integrate changes from one branch into another. 

25. What is GIT version control?
Ans : Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. For the examples in this book, you will use software source code as the files being version controlled, though in reality you can do this with nearly any type of file on a computer.

26. What is the function of ‘git diff ’ in git?.
Ans : Diffing is a function that takes two input data sets and outputs the changes between them. git diff is a multi-use Git command that when executed runs a diff function on Git data sources. These data sources can be commits, branches, files and more.

27. What is ‘git status’ is used for?
Ans : The git status command displays the state of the working directory and the staging area. It lets you see which changes have been staged, which haven't, and which files aren't being tracked by Git. Status output does not show you any information regarding the committed project history.

28. What is the difference between the ‘git diff ’and ‘git status’?
Ans : 'git diff ’ depicts the changes between commits, commit and working tree, etc. whereas ‘git status’ shows you the difference between the working directory and the index, it is helpful in understanding a git more comprehensively. ‘git diff’ is similar to ‘git status’, the only difference is that it shows the differences between various commits and also between the working directory and index. 

29. What is the function of ‘git checkout’ in git?
Ans : The git checkout command lets you navigate between the branches created by git branch . Checking out a branch updates the files in the working directory to match the version stored in that branch, and it tells Git to record all new commits on that branch.

30. What is the function of ‘git rm’?
Ans : The git rm command can be used to remove individual files or a collection of files. The primary function of git rm is to remove tracked files from the Git index. Additionally, git rm can be used to remove files from both the staging index and the working directory.

31. What is the function of ‘git stash apply’?
Ans : git stash temporarily shelves (or stashes) changes you've made to your working copy so you can work on something else, and then come back and re-apply them later on. 

32. What is the use of ‘git log’?
Ans : Git log is a utility tool to review and read a history of everything that happens to a repository. Multiple options can be used with a git log to make history more specific. Generally, the git log is a record of commits.

33. What is ‘git add’ is used for?
Ans : The git add command adds a change in the working directory to the staging area. It tells Git that you want to include updates to a particular file in the next commit. However, git add doesn't really affect the repository in any significant way—changes are not actually recorded until you run git commit .

34. What is the function of ‘git reset’?
Ans :  git reset is a powerful command that is used to undo local changes to the state of a Git repo. Git reset operates on "The Three Trees of Git". These trees are the Commit History ( HEAD ), the Staging Index, and the Working Directory.

35. Explain what is commit message?
Ans : What is a commit message? The commit command is used to save changes to a local repository after staging in Git. However, before you can save changes in Git, you have to tell Git which changes you want to save as you might have made tons of edits.

36. Name a few Git repository hosting services
Ans :  1. Amazon AWS COdeCommit 2. Assembla 3. Beanstalk 4. Bitbucket  5. Codebase 6. Fog Creek klin  7. Github 8. Gitlab 9. LunchPad 10. Microsoft Azure DevOps 11. SourceForge 12. Perforce 12. RhodeCode 13.Planio




 






