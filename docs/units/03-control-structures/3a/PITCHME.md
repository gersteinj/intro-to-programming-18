---
# Intro to Programming

#### Unit 3 Section A - Conditional Statements & Loops
---
## Do Now

Read the [Python documentation on if statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements) and see if you can create an if statement in a new Repl.it (no exercise for this one)
---
## Core Concepts

* Conditional statements
* Loops
---
# Conditional Statements
---
## Conditional statements

* *if* something is True, *then* do something
* *otherwise if* something is True, *then* do something
* *otherwise* do something
---
## Rules of Conditionals

* *if* is required
* *elif* and *else* are optional
* As soon as one clause has been run, Python skips the rest of the chain
---
## and/or/not

* *and* & *or* can combine two statements
* *and* is True if both sides are True
* *or* is True if either side is True
* *not* reverses True/False values
---
# Loops
---
## Try It

Exercise 3.0
---
## Loops

* Loops allow for controlled repetition
* Two styles of loops
* Both types of loops will run based on conditions
---
## While Loops

* *while* something is True *do* something
* while you have homework left to do, do homework
* while you're alive, breathe
* while you are in the water, swim
* **Watch out for infinite loops!**
---
## While loops

How does this compare to if statement?

```python
n = 0

while n <= 100:
    print(n)
    n += 1
```
---
## break

break is a keyword that will exit a loop

```python
n = 0

while True:
    print(n)
    n += 1

    if n == 100:
        break
```
---
## For loops

* *do* something *for each item* in a range
* for each student in the class, give chocolate to that student
* for each number from 0 through 99, print the number
---
## range

* The `range()` function generates a sequence of numbers
* `range(max)`
* `range(min, max)`
* `range (min, max, step)`
---
## For

```python
for x in range(101):
    print(x)
```

```python
people = ["Jen", "Jean", "Jim", "Bill", "Rick", "Audrey", "Kung"]

for person in people:
    print(f"Good morning {person}")
```