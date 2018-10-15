---
# Intro to Programming

#### Unit 3 Lesson H - Functions
---
## Do Now

Submit your work for hangman
---
## Core Concepts

* Functions
---
## Functions

* Predefined pieces of code
* Always return some value (even if it's None)
* Can define your own
---
## Anatomy of a Function

```python
def my_amazing_function(my_arguments):
    """This is a docstring and should always be included"""
    print("This is a simple function that just prints something")
    return
```
@[1](This line gives the function its name and define the arguments it will take)
@[2-4](The block of code will run when the function is called)
@[2](The docstring describes the function)
@[3-4](This is what the function does)
@[4](The function will exit even if you leave out return)
---
## Anatomy of a Function 2

```python
def my_amazing_function(power_to_use):
    """Calculate 2 raised to the power of the argument provided and return it"""
    result = 2 ** power_to_use
    return result
```
@[1](This line gives the function its name and define the arguments it will take)
@[2-4](The block of code will run when the function is called)
@[2](The docstring describes the function)
@[3-4](This is what the function does)
@[4](Return the value of result to the program)
---