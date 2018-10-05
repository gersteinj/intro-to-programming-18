---
# Intro to Programming

#### Unit 3 Section C - Hangman
---
# Hangman
---
## Required Work

* Pseudocode (submit in Google Classroom, must be typed)
* Flowchart (submit in Google Classroom as a .png, .jpg, or .pdf file, may be digital or scanned from paper)
* Code (work from project in Repl.it)
* Reflection (submit in Google Classroom, must be typed)
---
## Schedule

You will have this class and the class after it. Assignment is due at end of second class.
---
## Scoring

* Pseudocode: 5 points, based on correct depiction of how to solve the problem
* Flowchart: 10 points, based on correct depiction of how to solve the problem
* Code: 40 points
* Reflection: 5 points, describe what you learned, what problems you ran into, and how you solved your problems
---
## Rubric

| Category | 5 | 4 | 3 | 2 | 1 |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------|-----------------------------------------------------------------------|----------------------------------------------------|------------------------------|
| Requirements Weighted x3 | Has features beyond requirements given | Meets all given requirements | Meets most requirements | Meets a few requirements | Meets few to no requirements |
| Comments | Comments display a clear understanding of the code | Comments are mostly good but could be more informative | Some comments are present, but large sections of code are uncommented | Comments are minimal | Comments? What comments? |
| Code Quality Weighted x3 | Code is cleanly written and very effective. Code in this category will show that the coder has made an effort to address problems that could arise when running code. | Code is correct and generally free of errors | Some errors affect the functioning of the program | Major errors affect the functioning of the program | Code works extremely poorly |
| User Interface/User Experience | Program makes clear to the user what is happening and it is enjoyable to play. For instance, program has an effective way of tracking failed guesses. | Game is fairly easy to understand how to play | Playing game is somewhat confusing | Playing game is very confusing | Can't play game |
|  |  |  |  |  |  |
---
## Suggestions

* Break it into small sections and write your code a little at a time
* Test early, test often
* While testing, you can use print() to show what a value is
---
# Helpful Code and Code Patterns
---
## in

* The `in` operator checks to see if some object exists in a sequence
* Typically used with lists or strings
* `'n' in 'Magnet'` is a True statement
---
## Looping Through Strings

* Can use a for loop for each character in a string

```python
for letter in "New Jersey":
    print(letter)
```
@[2] Can you replace this with a conditional statement to print letters based on certain conditions?
---
## Checking Items in a Sequence

Sometimes, you want to check multiple things in a sequence. For instance, finding out if all the characters in a string are vowels.

```python
is_only_vowels = True

for char in "Sphinx of black quartz, judge my vow.":
    if char not in 'aeiou':
        all_vowels = False

if is_only_vowels:
    print("That was only vowels")
else:
    print("You had other characters")
```
---
## Logical tests without comparisons

A lot of you are trying to write logical tests without comparisons. For instance:

```python
for n in range(10):
    if n % 3:
        print(f"{n} is divisible by 3")
```

This will do the exact **opposite** of what you want. Without a comparison, your logical test is *only the number*.

O is evaluated as false, and non-zero numbers are evaluated as true, so that statement will only run when n is *not* divisible by 0!

Generally, we only leave out the comparison for a value/variable that has a value of either True or False