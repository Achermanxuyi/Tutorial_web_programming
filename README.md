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

The IDE will show the changes and their authors, you can choose the version you want or directly change the repository.

### git log

```powershell
git log
```

Give a history of all of your commits on that repository.

*To exit: press `Q` key*.

### git reset

Revert back to a previous commit.

```powershell
git reset --hard <commit>
git reset --hard origin/master
```

+ commit: revert your code to a exact version with commit hash code (seen in `git log`).

+ origin/master: revert your code to the version currently stored online on Github.

### Branching

+ Branching is a method of moving into a new direction when creating a new feature, and only combining this new feature with the main part of your code, or the main branch.

+ The branch you are currently looking at is determined by the `HEAD`, which points to one of the two branches. Nu default, the HEAD is pointed at the master branch, but we can check out other branches as well.

+ How to implement branching in our git repositories:

  + Run `git branch` to see which you are currently working on:
    ```powershell
    PS E:\Full Stack\Web Programming with Python and JavaScript\Code\Tutorial_web_programming> git branch
    * main
    ```

  + To make a new branch

    ```powershell
    git checkout -b <branch name>
    ```

  + Switch between branches.

    ```powershell
    git checkout <branch name>
    ```

    And commit any changes to each branch.

  + when we are ready to merge our branches together, we'll check out the branch we wish to keep (almost always the master branch).

    ```powershell
    git merge <othter branch name>
    ```


## Python

```python
print("Hello, world!")
```



### Variables

```python
a = 38 # integer
b = 1.5 # float
c = "Hello!" # str
d = True # bool
e = None # NoneType
```

### Formatting Strings

eg1.

```python
name = input("Name: ")
print("Hello, " + name)
```

eg2.

```python
print(f"Hello, {input('Name: ')}")
```

### Conditiions

```python
num = int(input("Number: "))
if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is 0")
```

### Sequences

One of the most powerful parts of the Python language is its ability to work with **sequences** of data in addition to individual variables.

#### Strings

**Ordered**: Yes

**Mutable**: No

We can think of a string as a sequence of characters, we can access individual elements within the string.

```python
name = "Harry"
print(name[0])
print(name[1])
```

#### Lists

**Ordered**: Yes

**Mutable**: Yes

A [Python list](https://www.w3schools.com/python/python_lists.asp) allows you to store any variable types. 

```python
# List
names = ["Harry", "Ron", "Hermione"]
# Print the entire list:
print(names)
# Print the second element of the list:
print(names[1])
# Add a new name to the list:
names.append("Draco")
# Sort the list:
names.sort()
# Print the new list:
print(names)
```

#### 

