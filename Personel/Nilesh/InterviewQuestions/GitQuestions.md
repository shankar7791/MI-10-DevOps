1)      What is GIT?
	Git is a free and open source distributed version control system design to handle everything from small to large projects with speed and efficiency.

2)      What is a repository in GIT?
	Repositories in git contain a collection of files of various different version of project.these files are imported from the repositories into the local server  of the user for further updations and modifications in the content of the file.

3)      What is the command you can use to write a commit message?
	Git commit -m “message”

4)      What is the difference between GIT and SVN?
	Git : Git is a distributed version control system.
	        Git deals with large number of files like binary files that change quickly thats why it become slow.
	        In git we create .git directory

	Svn : svn is centralized version control system.
                     Svn controls the large number of binary files easily.
	         In svn we create .svn directory in every folder.

5)      What are the advantages of using GIT?
	One of the biggest advantage of git is its branching capabilities.
	Git branches are cheap and easy to merge.
	
6)      What language is used in GIT?
	
7)      What is the function of ‘GIT PUSH’ in GIT?
	Git push command is used to upload local repository content to remote repository.

8)      Why GIT better than Subversion?
	Git has the advantage that its much better suited if some devlopers are not always.
	Connected to master repository.also its much faster than svn.

9)      What is “Staging Area” or “Index” in GIT?
	The git index is used as staging area between your working directory and your repository. You can use the index to build up set of changes that you want to commit together.

10)   What is GIT stash?
		Git stash temporarily shelves changes you have made to their working copy so you can work on something  else and then come back and reapply them later on.

11)   What is GIT stash drop?
Drop your stash remove the changes from your stash and reapplies the last saved date.

12)   How will you know in GIT if a branch has been already merged into master?
	Find las commit hash on master branch.
	Find last commit hash on a branch.
 	Run command git merge-base<commit- hash- step1><commit-hash-step2>
	if output of step 3 is same as output of step2 then a branch has been already merged into master.

13)   What is the function of git clone?
	git clone is primarily used to point to an existing repo and make a clone or copy of that repo at in a new directory, at another location.

14)   What is the function of ‘git config’?
	The git config command is a convenience function that is used to set Git configuration values on a global or local project level

15)   What does commit object contain?
	The commit object contains the directory tree object hash, parent commit hash, author, committer, date and message.

16)   How can you create a repository in Git?
	Go into the new directory
	type git init
	write some code
	type git add to add the files
	type git commit

17)   What is ‘head’ in git and how many heads can be created in a repository?
	A repository can contain any number of heads. When you checkout to any branch the HEAD revision changes to the latest commit of the new branch. We directly will not create head but when we commit, git creates a reference to that commit known as head.

18)   What is the purpose of branching in GIT?
	In Git, branches are a part of your everyday development process. Git branches are effectively a pointer to a snapshot of your changes. When you want to add a new feature or fix a bug no matter how big or how small you spawn a new branch to encapsulate your changes.

19)   What is the common branching pattern in GIT?
	Git it's common to create, work on, merge, and delete branches several times a day. You saw this in the last section with the iss53 and hotfix branches you created. 

20)   How can you bring a new feature in the main branch?
	First, you need to make sure your local master is synchronized with the upstream master . Then, you merge the feature branch into master and push the updated master back to the central repository.

21)   What is a ‘conflict’ in git?
	Git can handle most merges on its own with automatic merging features. A conflict arises when two separate branches have made edits to the same line in a file, or when a file has been deleted in one branch but edited in the other.

22)   How can conflict in git resolved?
	Open
	navigate into the local git repository and merge conflicts
	generate a list of the files affected by the merge conflicts.
	Open your favourite text editor  such as atom and navigate to the file that merge conflicts.
	Decide if you want to removed the file.
	
23)   To delete a branch what is the command that is used?
	run 'git branch -D my-branch'.

24)   What is another option for merging in git?
	Using git rebase Instead of git merge. Using the "git merge" command is probably the easiest way to integrate changes from one branch into another. However, it's not your only option: "git rebase" offers another, slightly different way of integration.

25)   What is GIT version control?
	Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later.

26)    What is the function of ‘git diff ’ in git?
	Diffing is a function that takes two input data sets and outputs the changes between them. git diff is a multi-use Git command that when executed runs a diff function on Git data sources.

27)     What is ‘git status’ is used for?
	The git status command displays the state of the working directory and the staging area. It lets you see which changes have been staged, which haven't, and which files aren't being tracked by Git.

28)   What is the difference between the ‘git diff ’and ‘git status’?
	“git diff --cached” or “git diff –staged” will compare the staged state and last commit state. Make this difference very clear, that “git diff” will only show you the difference, between the staged and current state. “git diff –staged” will show you the difference between your staged files and last commit.
29) What is the function of ‘git checkout’ in git?
	The git checkout command lets you navigate between the branches created by git branch . Checking out a branch updates the files in the working directory to match the version stored in that branch, and it tells Git to record all new commits on that branch.

30) What is the function of ‘git rm’?
	The git rm command can be used to remove individual files or a collection of files. The primary function of git rm is to remove tracked files from the Git index.
	
32)   What is the use of ‘git log’?
	Git log is a utility tool to review and read a history of everything that happens to a repository

33)   What is ‘git add’ is used for?
	Git add is used to add the files to repository or branch.

34) What is the function of ‘git reset’?
	To review, git reset is a powerful command that is used to undo local changes to the state of a Git repo. Git reset operates on "The Three Trees of Git".

35)   Explain what is commit message?
	He commit command is used to save changes to a local repository after staging in Git. However, before you can save changes in Git, you have to tell Git which changes you want to save as you might have made tons of edits

36)   Name a few Git repository hosting services
	gitlab
	bitbucket
	sourceforge
	launchpad

