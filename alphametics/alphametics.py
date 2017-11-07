#!/user/bin/env python
#_*_coding:utf-8_*_

import re
import itertools


def solve(puzzle):
    '''英文等式转换为数学成立等式，如i + love = you'''
    words = re.findall('[A-Z]+', puzzle.upper())
    unique_characters = set(''.join(words))
    assert len(unique_characters) <= 10, 'Too many letters'
    first_letters = {word[0] for word in words}  # 首字母对应的不能为0
    n = len(first_letters)
    # 把首字母放到前面以便后边判断
    sorted_charaters = ''.join(first_letters) + ''.join(unique_characters - first_letters)
    characters = tuple(ord(c) for c in sorted_charaters)
    digits = tuple(ord(c) for c in '0123456789')
    zero = digits[0]
    for guess in itertools.permutations(digits, len(characters)):
        if zero not in guess[:n]:  # 前n个数字里不出现0，那么首字母就没有0
            equation = puzzle.translate(dict(zip(characters, guess)))
            if eval(equation):
                return equation

if __name__ == '__main__':
    import sys
    for puzzle in sys.argv[1:]:
        print(puzzle)
        solution = solve(puzzle)
        if solution:
            print(solution)
