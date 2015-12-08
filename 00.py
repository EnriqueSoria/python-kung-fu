#! /usr/bin/env python

from __future__ import print_function

# Author: Victor Terron (c) 2015
# Email: `echo vt2rron1iaa32s | tr 132 @.e`
# License: GNU GPLv3

""" How do you determine whether a string is a permutation of another? """

import unittest

def is_permutation(word, another):
    # Set it to lower
    word, another = word.lower(), another.lower()

    # If they are empty
    if len(word) == 0 and len(another) == 0:
        return True

    def to_dict(string):
        d = dict()
        for char in string:
            if d.has_key(char):
                d[char] += 1
            else:
                d[char] = 1
        if d.has_key(" "):
            del d[" "]
        return d

    return to_dict(word) == to_dict(another)
    

class AllUniqueTests(unittest.TestCase):

  def test_all_unique(self):

    self.assertTrue (is_permutation("", ""))
    self.assertTrue (is_permutation("a", "a"))
    self.assertTrue (is_permutation("aab", "aba"))
    self.assertTrue (is_permutation("dog", "God"))
    self.assertTrue (is_permutation("Buckethead", "Death Cube K"))
    self.assertTrue (is_permutation("Quid est veritas", "Est vir qui adest"))
    self.assertFalse(is_permutation("draft", "soft"))
    self.assertFalse(is_permutation("master", "muster"))

if __name__ == "__main__":
    unittest.main()
