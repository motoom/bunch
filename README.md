Use dictionaries as if they were objects, using terse attritbute syntax instead of key lookups.
Saves typing a lot of quotes and square brackets!

Make it easy to use dot-attribute notation like 'd.name' instead of 'd["name"]'.

Suppose I have a dictionary `d = {"name": "Jean", "age": 27}`

after doing `p = Bunch(d)` I can use attributes:

`print "%s is %d year old" % (p.name, p.age)`

Also contains `bunched()` which returns a tuple of Bunch objects, given a sequence or collection of dictionaries.
