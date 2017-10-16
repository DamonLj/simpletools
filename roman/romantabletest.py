#!/user/bin/env python
# -*- coding: utf-8 -*-

"""Unit test for romantable.py"""

import romantable
import unittest


class KnownValues(unittest.TestCase):
    knownValues = ((1, 'I'),
                   (2, 'II'),
                   (3, 'III'),
                   (4, 'IV'),
                   (5, 'V'),
                   (6, 'VI'),
                   (7, 'VII'),
                   (8, 'VIII'),
                   (9, 'IX'),
                   (10, 'X'),
                   (50, 'L'),
                   (100, 'C'),
                   (500, 'D'),
                   (1000, 'M'),
                   (31, 'XXXI'),
                   (148, 'CXLVIII'),
                   (294, 'CCXCIV'),
                   (312, 'CCCXII'),
                   (421, 'CDXXI'),
                   (528, 'DXXVIII'),
                   (621, 'DCXXI'),
                   (782, 'DCCLXXXII'),
                   (870, 'DCCCLXX'),
                   (941, 'CMXLI'),
                   (1043, 'MXLIII'),
                   (1110, 'MCX'),
                   (1226, 'MCCXXVI'),
                   (1301, 'MCCCI'),
                   (1485, 'MCDLXXXV'),
                   (1509, 'MDIX'),
                   (1607, 'MDCVII'),
                   (1754, 'MDCCLIV'),
                   (1832, 'MDCCCXXXII'),
                   (1993, 'MCMXCIII'),
                   (2074, 'MMLXXIV'),
                   (2152, 'MMCLII'),
                   (2212, 'MMCCXII'),
                   (2343, 'MMCCCXLIII'),
                   (2499, 'MMCDXCIX'),
                   (2574, 'MMDLXXIV'),
                   (2646, 'MMDCXLVI'),
                   (2723, 'MMDCCXXIII'),
                   (2892, 'MMDCCCXCII'),
                   (2975, 'MMCMLXXV'),
                   (3051, 'MMMLI'),
                   (3185, 'MMMCLXXXV'),
                   (3250, 'MMMCCL'),
                   (3313, 'MMMCCCXIII'),
                   (3408, 'MMMCDVIII'),
                   (3501, 'MMMDI'),
                   (3610, 'MMMDCX'),
                   (3743, 'MMMDCCXLIII'),
                   (3844, 'MMMDCCCXLIV'),
                   (3888, 'MMMDCCCLXXXVIII'),
                   (3940, 'MMMCMXL'),
                   (3999, 'MMMCMXCIX'))

    def testToRomanKnownValues(self):
        """toRoman should give known result with known input"""
        for integer, numeral in self.knownValues:
            result = romantable.toRoman(integer)
            self.assertEqual(numeral, result)

    def testFromRomanKnownValues(self):
        """fromRoman should give known result with known input"""
        for integer, numeral in self.knownValues:
            result = romantable.fromRoman(numeral)
            self.assertEqual(integer, result)


class ToRomanBadInput(unittest.TestCase):
    def testTooLarge(self):
        """toRoman should faile with large input"""
        self.assertRaises(romantable.OutOfRangeError, romantable.toRoman, 4000)

    def testZero(self):
        """toRoman should faile with 0 input"""
        self.assertRaises(romantable.OutOfRangeError, romantable.toRoman, 0)

    def testNegative(self):
        """toRoman should faile with negative input"""
        self.assertRaises(romantable.OutOfRangeError, romantable.toRoman, -1)

    def testNonInteger(self):
        """toRoman should faile with non-integer input"""
        self.assertRaises(romantable.NotIntegerError, romantable.toRoman, 0.5)


class FromRomanBadInput(unittest.TestCase):
    def testTooManyRepeatedNumerals(self):
        """fromRoman should faile with too many repeated numerals"""
        for s in ('MMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
            self.assertRaises(romantable.InvalidRomanNumeralError, romantable.fromRoman, s)

    def testRepeatedPairs(self):
        """fromRoman should faile with too many pairs of numerals"""
        for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
            self.assertRaises(romantable.InvalidRomanNumeralError, romantable.fromRoman, s)

    def testMalformedAntecedent(self):
        """fromRoman should faile with malformed antecendents"""
        for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
                  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
            self.assertRaises(romantable.InvalidRomanNumeralError, romantable.fromRoman, s)

    def testBlank(self):
        """fromRoman should faile with blank string"""
        self.assertRaises(romantable.InvalidRomanNumeralError, romantable.fromRoman, "")


class SanityCheck(unittest.TestCase):
    def testSanity(self):
        """fromRoman(toRoman(n))==n for all n"""
        for integer in range(1, 4000):
            numeral = romantable.toRoman(integer)
            result = romantable.fromRoman(numeral)
            self.assertEqual(integer, result)


class CaseCheck(unittest.TestCase):
    def testToRomanCase(self):
        """toRoman should always return uppercase"""
        for integer in range(1, 4000):
            numeral = romantable.toRoman(integer)
            self.assertEqual(numeral, numeral.upper())

    def testFromRomanCase(self):
        """fromRoman should only accept uppercase input"""
        for integer in range(1, 4000):
            numeral = romantable.toRoman(integer)
            romantable.fromRoman(numeral.upper())
            self.assertRaises(romantable.InvalidRomanNumeralError, romantable.fromRoman, numeral.lower())

if __name__ == "__main__":
    unittest.main()
