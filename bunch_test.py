import unittest
from bunch import Bunch, bunched

class TestBunch(unittest.TestCase):

    def testCreation(self):
        d = dict(firstname="Joe", lastname="Doe", age=27, phone="06-8239.43.12", email="joe@zom.com")
        p = Bunch(d)
        self.assertEqual("%s is %d years old" % (p.firstname, p.age), "Joe is 27 years old")
        self.assertEqual(str(p), "age: 27\nemail: 'joe@zom.com'\nfirstname: 'Joe'\nlastname: 'Doe'\nphone: '06-8239.43.12'")
        self.assertEqual(repr(p), repr(d))  # Something like the following, but keys not in order "{'phone': '06-8239.43.12', 'age': 27, 'email': 'joe@zom.com', 'firstname': 'Joe', 'lastname': 'Doe'}"
        self.assertEqual(p.firstname, "Joe")  # access as attribute
        self.assertEqual(p["firstname"], "Joe")  # access like a dictionary

        def fetch_unknown_attribute():
            return p.nonexistant

        def fetch_unknown_key():
            return p["nonexistant"]

        self.assertRaises(AttributeError, fetch_unknown_attribute)
        self.assertRaises(KeyError, fetch_unknown_key)


    def testAssignmentFetch(self):
        d = dict(firstname="Joe", lastname="Doe", age=27, phone="06-8239.43.12", email="joe@zom.com")
        p = Bunch(d)
        p["taste"] = "sweet"  # item assignment like a dictionary
        p.aftertaste = "bitter"  # attribute assignment

        self.assertEqual(p.taste, "sweet")
        self.assertEqual(p.aftertaste, "bitter")
        self.assertEqual(p["taste"], "sweet")
        self.assertEqual(p["aftertaste"], "bitter")
        

    def testUpdate(self):
        d = dict(article="box")
        p = Bunch(d)

        dimensions = dict(length=3, weigth=13)
        p.update(dimensions)

        self.assertEqual(p.weigth, 13)
        self.assertEqual(p["weigth"], 13)

        base = Bunch(a=1, b=2)
        extradict = dict(c=3, d=4)
        extrabunch = Bunch(e=5, f=6)
        base.update(extradict)
        base.update(extrabunch)

        self.assertEqual(base.c, 3)
        self.assertEqual(base.f, 6)
        

    def testCopy(self):
        orig = Bunch()
        orig.a = "Alice"

        copy = Bunch(orig)
        copy.a = "Bob"

        self.assertEqual(orig.a, "Alice")
        self.assertEqual(copy.a, "Bob")

        self.assertNotEqual(orig.a, copy.a)
        self.assertIsNot(orig.a, copy.a)


    def testBunched(self):
        ds = (
            dict(name="Joe", age=27),
            dict(name="Sue", age=21),
            dict(name="Peter", age=56)
            )

        ps = bunched(ds)
        self.assertEqual(ps[0].name, "Joe")
        self.assertEqual(ps[1].name, "Sue")
        self.assertEqual(ps[2].name, "Peter")
        
        es = bunched([])
        self.assertIsInstance(es, tuple)
        self.assertEqual(len(es), 0)


    def testBooleanContexts(self):
        n = Bunch(None)
        t = Bunch(dict(a=1))
        f = Bunch(dict())
        k = Bunch(a=1, b=2, c=3)

        self.assertFalse(n)
        self.assertFalse(f)
        self.assertTrue(t)
        self.assertTrue(k.b == 2)

        e = Bunch()
        self.assertFalse(e)
        e.color = "yellow"
        self.assertTrue(e)


def main():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBunch)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == "__main__":
    main()
