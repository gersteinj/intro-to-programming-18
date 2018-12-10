---
# Intro to Programming

#### Unit 2 Section D - Creating your first repository
---
# Version Control
---
## Do Now


---
## Vocab

* Repository
* Remote Repository
* Local Repository
* Directory
* Working Directory
* Command Prompt
* Shell
---
# GitHub/Git
---
## GitHub

* Remote repository host
* Adds additional features
* Makes your repository available from anywhere with internet access
* Web interface, graphical interface, command line
---
## Git

* The actual version control system
* Command line only
---
## Set up Git

```bash
14:35 ~ $ git config --global user.name <yourname>
14:35 ~ $ git config --global user.email <youremail>
14:35 ~ $ git config --global credential.helper cache
```
---
## Local Git Commands

* `init`
* `add`
* `commit`
* `local`
* `checkout`
* `branch`
* `merge`
* `reset`
---
## Remote Git Commands

* `clone`
* `push`
* `pull`
---
## INIT

* Create repository from CWD

```bash
14:35 ~ $ git init
```
---
## CLONE

* Make local copy of remote repository in CWD

```bash
14:35 ~ $ git clone <url>
```
---
## Try It

* Go to GitHub
* Create a repository called "first-repo"
* Get the clone URL
* Clone in PythonAnywhere
* Use your command line commands to navigate into your new first-repo directory
---
## ADD

* Add files to staging area
* Many different ways to use

```bash
14:35 ~ $ git add <filename>        # Stage <filename>
14:35 ~ $ git add <directoryname>   # Stage all files in <directoryname>
14:35 ~ $ git add .                 # Stage all modified and deleted files
14:35 ~ $ git add -A                # Stage all (new, modified, deleted) files
```
---
## Try It

* Create a few new files in your local respository
* Use `git status` to check your repo
* Stage your new files
* Use `git status` again to check your repo
---
## COMMIT

* Create a snapshot
* Can create a commit message at same time (recommended)

```bash
14:35 ~ $ git commit                    # Creates a commit
14:35 ~ $ git commit -a                 # Creates a commit, automatically staging all modified files
14:35 ~ $ git commit -m "message"       # Creates a commit with the specified commit message
# How could you automatically stage all modified files AND create a commit message
```
---
## Try It

* Create a commit with the message "First Commit"
* Use `git status` again to check your repo
---
## PUSH

* Send commits to remote repository
* First push may require setting upstream

```bash
14:35 ~ $ git push                      # Creates a commit
14:35 ~ $ git push --set-upstream origin master  # Creates a commit, automatically staging all modified files
```
---
## Try It

* Push your repository
* Go to GitHub to see your changes
---
## PULL

* Get commits from remote repository
* Always start with `git pull` if there's *any chance* the remote repo has been updated

```bash
14:35 ~ $ git pull
```
---
## Try It

* Use GitHub's web interface to change the README.md file
* Use `git status` to see current state of local repo
* Use `git pull` to get newest updates
* Use `git status` again to see current state of local repo