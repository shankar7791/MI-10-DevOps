1)	What is GIT?

GIT is a distributed version control system and source code management (SCM) system with an emphasis to handle small and large projects with speed and efficiency.

2)      What is a repository in GIT?

A repository contains a directory named .git, where git keeps all of its metadata for the repository. The content of the .git directory are private to git.

3)      What is the command you can use to write a commit message?

git commit -m "Message"

4)      What is the difference between GIT and SVN?

The difference between Git and SVN version control systems is that Git is a distributed version control system, whereas SVN is a centralized version control system.Git uses multiple repositories including a centralized repository and server, as well as some local repositories. SVN does not have a centralized repository or server. 
Git is less preferred for handling extremely large files or frequently changing binary fileswhile SVN can handle multiple projects stored in the same repository
GIT does not support ‘commits’ across multiple branches or tags.  Subversion allows the creation of folders at any location in the repository layout.
Gits are unchangeable, while Subversion allows committers to treat a tag as a branchand to create multiple revisions under a tag root

5)	What are the advantages of using GIT?

a)Data redundancy and replication
b)High availability
c)Only one.git directory per repository
d)Superior disk utilization and network performance
e)Collaboration friendly
f)Any sort of projects can use GIT

6)      What language is used in GIT?

GIT is fast, and ‘C’ language makes this possible by reducing the overhead of run time sassociated with higher languages

7)      What is the function of ‘GIT PUSH’ in GIT?

The git push command is used to upload local repository content to a remote repository.

8)      Why GIT better than Subversion?

GIT is an open source version control system; it will allow you to run ‘versions’ of a project,which show the changes that were made to the code overtime also it allows you keep thebacktrack if necessary and undo those changes.  Multiple developers can checkout, and uploadchanges and each change can then be attributed to a specific developer.

9)      What is “Staging Area” or “Index” in GIT?

Before completing the commits, it can be formatted and reviewed in an intermediate area known as ‘Staging Area’ or ‘Index’

10)	What is GIT stash?

GIT stash takes the current state of the working directory and index and puts in on the stack forlater and gives you back a clean working directory.  So in case if you are in the middle ofsomething and need to jump over to the other job, and at the same time you don’t want to lose your current edits then you can use GIT stash.


11)	What is GIT stash drop?

When you are done with the stashed item or want to remove it from the list, run the git ‘stashdrop’ command.  It will remove the last added stash item by default, and it can also remove aspecific item if you include as an argument.

12)	How will you know in GIT if a branch has been already merged into master?

Git branch---merged lists the branches that have been merged into the current branch
Git branch----no merged lists the branches that have not been merged

13)	What is the function of git clone?

The git clone command creates a copy of an existing Git repository.  To get the copy of acentral repository, ‘cloning’  is the most common way used by programmers.

14)	What is the function of ‘git config’?

The ‘git config’ command is a convenient way to set configuration options for your Gitinstallation.  Behaviour of a repository, user info, preferences etc. can be defined through thiscommand.

15)	What does commit object contain?

a) A set of files, representing the state of a project at a given point of time
b) Reference to parent commit objects
c) An SHAI name, a 40 character string that uniquely identifies the commit object.

16)	How can you create a repository in Git?

In Git, to create a repository, create a directory for the project if it does not exist, and then runcommand “git init”. By running this command .git directory will be created in the projectdirectory, the directory does not need to be empty.

17)	What is ‘head’ in git and how many heads can be created in a repository?

A ‘head’ is simply a reference to a commit object. In every repository, there is a default headreferred as “Master”.  A repository can contain any number of heads

18)	What is the purpose of branching in GIT?

The purpose of branching in GIT is that you can create your own branch and jump betweenthose branches. It will allow you to go to your previous work keeping your recent work intact.

19)	What is the common branching pattern in GIT?

The common way of creating branch in GIT is to maintain one as “Main“branch and create another branch to implement new features. This pattern is particularly useful when there are multiple developers working on a single project.

20)	How can you bring a new feature in the main branch?

To bring a new feature in the main branch, you can use a command “git merge” or “git pullcommand”

21)	What is a ‘conflict’ in git?

A ‘conflict’ arises when the commit that has to be merged has some change in one place, andthe current commit also has a change at the same place. Git will not be able to predict whichchange should take precedence

22)	How can conflict in git resolved?

To resolve the conflict in git, edit the files to fix the conflicting changes and then add theresolved files by running “git add” after that to commit the repaired merge,  run “git commit”. Git remembers that you are in the middle of a merger, so it sets the parents of the commitcorrectly

23)	To delete a branch what is the command that is used?

Once your development branch is merged into the main branch, you don’t needdevelopment branch.  To delete a branch use, the command “git branch –d [head]”

24)   	What is another option for merging in git?

“Rebasing” is an alternative to merging in git

25)     What is GIT version control?

With the help of GIT version control, you can track the history of a collection of files and includesthe functionality to revert the collection of files to another version.  Each version captures asnapshot of the file system at a certain point of time. A collection of files and their completehistory are stored in a repository.

26)     What is the function of ‘git diff ’ in git?

‘git diff ’ shows the changes between commits, commit and working tree etc

27)     What is ‘git status’ is used for?

As ‘Git Status’ shows you the difference between the working directory and the index, it ishelpful in understanding a git more comprehensively.

28)     What is the difference between the ‘git diff ’and ‘git status’?

git diff’ is similar to ‘git status’, but it shows the differences between various commits andalso between the working directory and index

29)     What is the function of ‘git checkout’ in git?

A ‘git checkout’ command is used to update directories or specific files in your working treewith those from another branch without merging it in the whole branch.

30)     What is the function of ‘git rm’?

To remove the file from the staging area and also off your disk ‘git rm’ is used.

31)     What is the function of ‘git stash apply’?

When you want to continue working where you have left your work, ‘git stash apply’ commandis used to bring back the saved changes onto the working directory.
 
32)     What is the use of ‘git log’?

To find specific commits in your project history- by author, date, content or history ‘git log’ isused

33)     What is ‘git add’ is used for?

git add’ adds file changes in your existing directory to your index

34)     What is the function of ‘git reset’?

The function of ‘Git Reset’ is to reset your index as well as the working directory to the state ofyour last commit.

35)     Explain what is commit message?

You want to have good commit messages that provide you useful information about what has changed and why

36)     Name a few Git repository hosting services

Pikacode 
Visual Studio Online 
GitHub 
GitEnterprise 
SourceForge.net

