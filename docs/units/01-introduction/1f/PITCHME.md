---
# Intro to Programming

#### Unit 1 Section G - Conditional Statements
---
## Do Now

Read the [Python documentation on if statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements) and see if you can create an if statement in a new Repl.it (no exercise for this one)
---
## Core Concepts

* Conditional statements
---
# Conditional Statements
---
## if

*if* some condition is true *then* do some action

```python
x = 5

if x % 2 == 0:
    print(f"{x} is even")
```
@[3](Logical test - will evaluate to determine True or False)
@[4](Block of code will run if logical test is evaluated as True)
---
## else

*if* some condition is true *then* do some action
*otherwise* do something else

```python
x = 5

if x % 2 == 0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")
```
@[5-6](If the 'if' statement does not run, 'else' will automatically run. Note that it doesn't have a logical test)
---
## elif

*if* some condition is true *then* do some action
*otherwise if* some condition is true *then* do some action
*otherwise* do something else

```python
x = 5

if x > 10:
    print(f"{x} is a big number!")
elif x < 0:
    print(f"{x} is a small number!")
else:
    print(f"{x} is of moderate size.")
```
@[3-4](This is checked first)
@[5-6](This is checked if the if doesn't run)
@[7-8](This will run if none of the above statements run)
---