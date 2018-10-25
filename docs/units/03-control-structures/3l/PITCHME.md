---
# Intro to Programming

#### Unit 3 Lesson L - Dictionaries
---
## Do Now

Repl.it review exercise
---
## Core Concepts

* Dictionaries
* Keys
* Values
---
## Question

How might you be able to keep track of a person's age, eye color, and hair color? What if there were multiple people to keep track of?
---
## Example

```python
# name = age, eye, hair
lauren = [33, 'brown', 'brown']
jim = [32, 'brown', 'black']
jen = [35, 'grey', 'blonde']

jen[0] # What is this? How do we know?
```
---
## Example

```python
names = ['lauren', 'jim', 'jen']
ages = [33, 32, 25]
eyes = ['brown', 'brown', 'grey']
hair = ['brown', 'black', 'blonde']

print(f"{names[0]} is {ages[0]} and has {eyes[0]} eyes and {hair[0]} hair")
```
---
## Lists of data

In the previous examples, how well did our lists work? Did they store the data? Was it easy to refer to?

Would it be easier if you could use `jim['hair']` to refer to Jim's hair color?
---
## Dictionaries

* Unordered list of key value pairs
* Refer to values using the associated key
* Keys must be unique strings
---
## Example

```python
jen = {'age': 35, 'hair': 'blonde', 'eyes': 'grey'}
jim = {'age': 32, 'hair': 'black', 'eyes': 'brown'}
lauren = {'age': 33, 'hair': 'brown', 'eyes': 'brown'}

print(f"Jen is {jen['age']} years old, with {jen['hair']} hair and {jen['eyes']} eyes.")
```
---
## Working with Dicts

* `d[key]`
* `d[key] = value`
* `d.keys()`
* `d.values()`
* `d.items()`
---
## Working with Dicts

* `len(d)`
* `key in d`
* `d.get(key[, default])`
---
```python
jim = {'age': 32, 'hair': 'black', 'eyes': 'brown'}

for k in jim.keys():
    print(k)

for v in jim.values():
    print(v)

for k, v in jim.items():
    print(f"Jim's {k}: {v}")
```