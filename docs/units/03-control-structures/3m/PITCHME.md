---
# Intro to Programming

#### Unit 3 Lesson M - Dictionaries
---
## Do Now

Imagine you were creating a game with an inventory system for the player. How might you organize the inventory?
---
## Core Concepts

* Dictionaries
* Keys
* Values
---
## Dictionaries

* Unordered list of key-value pairs
* Access items like lists, but refer to key instead of an index
---?code=docs/units/03-control-structures/3m/basicexample.py&lang=python

@[1-7](A sample dictionary. Can condense onto one line, but formatted for ease of reading)
@[10, 14](Print number of apples. Access a value with its keys)
@[12](Change value associated with apples)
@[17, 19](Add flour to inventory and print the value associated with it. If flour existed already, value would have been modified)
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
-----?code=docs/units/03-control-structures/3m/nestedexample.py&lang=python

@[2-6](Each person's name is a key in the main dictionary. The value is another dictionary)
@[5, 10, 15](Even within the second dictionary, one of the keys is a list)
@[19](What will be printed?)
@[20](What will be printed?)
@[21](What will be printed?)