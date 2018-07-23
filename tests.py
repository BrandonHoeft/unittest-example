#import os
#if os.getcwd() != '/Users/bhoeft/Desktop/unittest-example':
#    os.chdir('/Users/bhoeft/Desktop/unittest-example')
import unittest
from longest_word import longest_word


class MyTests(unittest.TestCase):
    
    def test_longest_word(self):
        s = "I need antihistamines during spring season."
        result = longest_word(s)
        self.assertEqual(result, "antihistamines")
        
    def test_ties_return_1st(self):
        """testing that 2 longest words will return the 1st."""
        s = "Tomatoes Potatoes"
        result = longest_word(s)
        self.assertEqual(result, "Tomatoes")
    
    def test_remove_punc(self):
        s = "Brandon!`~!@#$%^&*()-=+[]{}\|<>,.?/"
        result = longest_word(s)
        self.assertEqual(result, "Brandon")


if __name__  == '__main__':
    unittest.main()




# References: https://cgoldberg.github.io/python-unittest-tutorial/    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
