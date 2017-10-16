#!/user/bin/env python
# -*- coding: utf-8 -*-

"""Conbert to and from Roman numerals"""
import re


# Defin exceptions
class RomanError(Exception):pass
class OutOfRangeError(RomanError):pass
class NotIntegerError(RomanError):pass
class InvalidRomanNumeralError(RomanError):pass

# Define digit mapping
romanNumeralMap = (('M', 1000),
                   ('CM', 900),
                   ('D', 500),
                   ('CD', 400),
                   ('C', 100),
                   ('XC', 90),
                   ('L', 50),
                   ('XL', 40),
                   ('X', 10),
                   ('IX', 9),
                   ('V', 5),
                   ('IV', 4),
                   ('I', 1))

# Create tables for fast conversion of roman numerals.
# See fillLookupTables() below.
toRomanTable = [None]  # Skip an index since Roman numerals have no zero
fromRomanTable = {}


def toRoman(n):
    """convert integer to Roman numeral"""
    if not (0 < n < 4000):
        raise OutOfRangeError("number out of range(must be 1...3999")
    if int(n) != n:
        raise NotIntegerError("non-integer can not be converted")

    result = ''
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result

# Defin pattern to detect valid Roman numerals
romanNumeralPattern = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')


def fromRoman(s):
    """convert Roman numeral to integer"""
    if not s:
        raise InvalidRomanNumeralError("Input can not be blank")
    if not romanNumeralPattern.search(s):
        raise InvalidRomanNumeralError("Invalid Roman numeral:%s" % s)

    result = 0
    index = 0
    for numeral, integer in romanNumeralMap:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result
