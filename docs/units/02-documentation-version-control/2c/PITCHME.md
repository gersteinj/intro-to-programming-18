---
# Intro to Programming

#### Unit 2 Section C - Version Control Hands On
---
# Version Control
---
## Do Now

* Sign up for accounts at [GitHub](http://www.github.com) and [PythonAnywhere](http://www.pythonanywhere.com) using your school email address
* Make sure you know your password because you'll need it, especially the GitHub password
* Submit your GitHub and PythonAnywhere usernames [here](https://airtable.com/shr3i6UdKgdjeXsRy)
---
## PythonAnywhere

* Full Linux installation you can user in a browser
* Command line **only**
* Can use Git
---
## GitHub

* Online service for hosting remote repositories
* Widely used, especially for open source software
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
# Command Line
---
## Navigating Filesystem

Command prompt shows working directory

Windows:
```bash
C:\Users\gerst\Documents\GitHub\intro-to-programming-18>
```

Linux:
```bash
14:14 ~ $ 
14:14 ~ $ cd ProjectEuler
14:15 ~/ProjectEuler $ 
```
---
## Common Shell Commands

* `cd`
* `dir` & `ls`
* `rm` (Linux) or `del` (Windows)
* `mkdir`
* most commands can take arguments
---
## LS or DIR

* View contents of current working directory (CWD)

```bash
14:24 ~ $ ls
Day08.py        IntroToProgramming17  Notebook2.ipynb  README.txt        filescript.py  hello.py        processusernames.ipynb  pythagoras.py
FinalProject17  Notebook1.ipynb       PRS-stats        class_samples.py  first-repo     intro-to-lists  processusernames.py     usernames.csv

14:24 ~ $ dir
Day08.py        IntroToProgramming17  Notebook2.ipynb  README.txt        filescript.py  hello.py        processusernames.ipynb  pythagoras.py
FinalProject17  Notebook1.ipynb       PRS-stats        class_samples.py  first-repo     intro-to-lists  processusernames.py     usernames.csv

14:24 ~ $ 
```
---
## CD

* Used to change current working directory (CWD)
* `cd ..` will go up a level
* `cd ~` will go to home directory (on Linux)
* `cd <dirname>` will go to specified directory if contained in CWD

```bash
14:25 ~ $ ls
Day08.py        IntroToProgramming17  Notebook2.ipynb  README.txt        filescript.py  hello.py        processusernames.ipynb  pythagoras.py
FinalProject17  Notebook1.ipynb       PRS-stats        class_samples.py  first-repo     intro-to-lists  processusernames.py     usernames.csv

14:25 ~ $ cd ..
14:25 /home $ ls
gersteinj   jgerstein

14:25 /home $ cd ~
14:26 ~ $ cd first-repo
14:26 ~/first-repo (master)$ ls
pumpkin.py  readme.md
14:26 ~/first-repo (master)$ cd ..
14:26 ~ $ cd ..
14:26 /home $ ls
gersteinj   jgerstein
14:26 /home $ cd ~
14:26 ~ $ 
```
---
## MKDIR

* Create a directory (folder) in CWD

```bash
14:26 ~ $ mkdir SAMPLEDIR
14:35 ~ $ ls
Day08.py        IntroToProgramming17  Notebook2.ipynb  README.txt  class_samples.py  first-repo  intro-to-lists          processusernames.py  usernames.csv
FinalProject17  Notebook1.ipynb       PRS-stats        SAMPLEDIR   filescript.py     hello.py    processusernames.ipynb  pythagoras.py
14:35 ~ $ 
```
---
## RM (or DEL)

* Delete a directory or file in CWD
* `rm -rf <dirname>` to delete folder
* `rm <filename>` to delete file

```bash
14:35 ~ $ rm -rf SAMPLEDIR
14:36 ~ $ ls
Day08.py        IntroToProgramming17  Notebook2.ipynb  README.txt        filescript.py  hello.py        processusernames.ipynb  pythagoras.py
FinalProject17  Notebook1.ipynb       PRS-stats        class_samples.py  first-repo     intro-to-lists  processusernames.py     usernames.csv
14:36 ~ $ 
```
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
## Beginner Commands

* `init`
* `clone`
* `add`
* `commit`
* `checkout`
* `branch`
* `merge`
* `reset`
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
# Try It
---
## Set up Git

```bash
14:35 ~ $ git config --global user.name <yourname>
14:35 ~ $ git config --global user.email <youremail>
14:35 ~ $ git config --global credential.helper cache
```
---
## Clone

* Clone my sample repository <https://github.com/jgerstein/samplerepo2018.git>
* What's the command?