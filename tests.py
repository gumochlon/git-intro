#!/usr/bin/env python

# Reference: https://docs.python.org/library/unittest

import unittest

import primes


class PrimeTest(unittest.TestCase):

    def test_20(self):
        self.assertEqual(primes.primes(20), [2, 3, 5, 7, 11, 13, 17, 19])

if __name__ == '__main__':
    unittest.main()
