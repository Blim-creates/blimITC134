import unittest



#########
##This is where the unit test goes thats within the function

#function Testing the string with unittest import
class TestStringMethods(unittest.TestCase):
#testing uppercase strings
    def test_upper(self):
        #in self if the string is upper case, the test will pass
        self.assertEqual('foo'.upper(), 'FOO')
#testing is upper case is true or false
    def test_isupper(self):
#Condition to test if text string is 'FOO' then it's True
        self.assertTrue('FOO'.isupper())
#Condition to test if text string is 'Foo' then it's False
        self.assertFalse('Foo'.isupper())

#testing if there's a space between hello world
    def test_split(self):
#variable text string
        s = 'hello world'
#conditional statement to test for the split between hello and world
        self.assertEqual(s.split(), ['hello', 'world'])
        #check that s.split fails when the seperator is not a string

        with self.assertRaises(TypeError):
            s.split(2)

#calling the main function to execute the functions above
if __name__ == '__main__':
    unittest.main()