"""
bunch.py - Software by Michiel Overtoom, motoom@xs4all.nl

Use dictionaries as if they were objects, using terse attritbute syntax instead of key lookups.
Saves typing a lot of quotes and square brackets!

Make it easy to use dot-attribute notation like 'd.name' instead of 'd["name"]'.

Suppose I have a dictionary `d = {"name": "Jean", "age": 27}`

after doing `p = Bunch(d)` I can use attributes:

`print "%s is %d year old" % (p.name, p.age)`

Also contains `bunched()` which returns a tuple of Bunch objects, given a sequence or collection of dictionaries.
"""

class Bunch(object):
    """Object wrapper for a dictionary."""
    def __init__(self, initial=None, **kwargs):
        if isinstance(initial, Bunch):
            self.__dict__ = dict(initial.__dict__)
        elif isinstance(initial, dict):
            self.__dict__ = initial
        if kwargs:
            self.__dict__.update(kwargs)

    def __getitem__(self, key):
        """Makes subscriptability working (name = person["firstname"])"""
        return self.__dict__[key]

    def __setitem__(self, key, value):
        """Makes item assignment possible (person["age"] = 27)"""
        self.__dict__[key] = value

    def __len__(self):
        return len(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

    def __str__(self):
        s = ""
        for k in sorted(self.__dict__.keys()):
            v = self.__dict__[k]
            if isinstance(v, basestring):
                if len(v) > 50:
                    v = v[:50] + "..."
            s += "%s: %r\n" % (k, v)
        return s.strip()

    def update(self, other):
        if isinstance(other, Bunch):
            self.__dict__.update(other.__dict__)
        else:
            self.__dict__.update(other)

    def get(self, key, default=None):
        return self.__dict__.get(key, default)


def bunched(dicts):
    """Return a tuple of Bunch objects, given a collection or sequence of dictionaries."""
    return tuple(Bunch(d) for d in dicts)


if __name__ == "__main__":
    import bunch_test
    bunch_test.main()
        