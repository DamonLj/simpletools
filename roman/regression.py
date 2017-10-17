#!/user/bin/env python
# -*- coding: utf-8 -*-

"""回归测试框架
该模块将搜索名为同一目录的脚本
XYZtest.py。 每个这样的脚本应该是测试一个测试套件
模块通过PyUnit。 （从Python 2.1开始，PyUnit包含在
标准库为“unittest”。）
此脚本将聚合所有将测试套件发现到一个大的测试套件中，并一次性运行它们。
"""

import sys, os, re, unittest


def regressionTest():
    path = os.getcwd()
    sys.path.append(path)
    files = os.listdir(path)
    test = re.compile(r'test\.py$', re.IGNORECASE)
    files = filter(test.search, files)
    moduleNames = map(lambda f: os.path.splitext(f)[0], files)
    modules = map(__import__, moduleNames)
    load = unittest.defaultTestLoader.loadTestsFromModule
    return unittest.TestSuite(map(load, modules))


if __name__ == '__main__':
    unittest.main(defaultTest='regressionTest')
