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
    for plural_rule in rules:
        # return plural_rule(word) and plural_rule(word) or None  # 直接退出循环了
        if plural_rule(word):
            return plural_rule(word)
    raise ValueError("no matching rule for {0}".format(word))


class LazyRules(object):
    '''建立有缓存机制的rules,文件会一直被打开，直到被读取完或销毁类实例。'''
    def __init__(self, language='en'):
        self.rule_filename = 'pluralrule.{0}'.format(language)
        self.pattern_file = open(self.rule_filename, encoding='utf-8')
        self.cache = []

    def __iter__(self):
        self.cache_index = 0  # 每次用for调用，将读取缓存的下标初始化
        return self

    def __next__(self):
        self.cache_index += 1
        # 如果缓存列表中已经产生足够的缓存，那么下式为真，则直接调用缓存。index每次会被for初始化！
        if len(self.cache) >= self.cache_index:
            return self.cache[self.cache_index - 1]

        if self.pattern_file.closed:
            raise StopIteration

        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration

        pattern, search, replace = line.split(None, 3)
        funcs = lambda word: re.search(pattern, word) and re.sub(search, replace, word)
        self.cache.append(funcs)
        return funcs

rules = LazyRules()
