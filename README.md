# Tutorial_web_programming
**Course: Web Programming with Python and JavaScript**
*This is the note of  the course "Web Programming with JavaScript and Python"*
+ IDE: VS code (extensions required)
+ Language: HTML, css, scss, JavaScript, Python

## Git

### git clone

```
git clone <url>
```

**Download the repository to the local computer.**



In vs code terminal, 

```powershell
code filename.extension
```

to create a new file in current project folder.

eg.

```powershell
code hello.html
```

Then a file called "hello.html" is created successfully.

### git add

```powershell
git add <filename>
```

Track the file, so this file and the changes being made will be saved next time.

```powershell
git add .
```

Track all files within the directory.

### git commit

```powershell
git commit -m "message"
```

Save the current state of files.

"message": descriptions of changes you've made in the most recent commit files.

If you commit all of the file that have been changed at the same time, use:

```powershell
git commit -am "message"
```

### git status

```powershell
git status
```

Report current repository status.

### git push

```powershell
git push
```

Publish your local commits to github.

### git pull

```
git pull
```

Sometimes, the remote repository on GitHub will be more up to date than the local version. In this cade, you want to first commit any changes then run `git pull` to pull any remote changes to your local repository.

### Merge Conflicts

+ One problem that can emerge when working with Git, especially when you're collaborating with other people, is something called a **merge conflict**. A merge conflict occurs when two people attempt to change a file in ways that conflict with each other.
+ This will typically occur when you either `git push` or `git pull`. When this happens, Git automatically change into a format that clearly outlines what the conflict is. 

