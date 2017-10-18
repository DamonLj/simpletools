#!/user/bin/env python
# -*- coding: utf-8 -*-

import re


def rule(language):
    with open('pluralrule.%s' % language, encoding='utf-8') as pattern_file:
        for line in pattern_file:  # open()产生的对象本身就是生成器，循环返回每行。
            pattern, search, replace = line.split()
            # yield产生判断和执行函数，and前判断，False则False；都是True，则输出后者。
            yield lambda word: re.search(pattern, word) and re.sub(search, replace, word)


def plural(word, language='en'):
    for plural_rule in rule(language):
        # return plural_rule(word) and plural_rule(word) or None  # 直接退出循环了
        if plural_rule(word):
            return plural_rule(word)
    raise ValueError("no matching rule for {0}".format(word))
