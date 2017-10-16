#!/user/bin/env python
#_*_coding:utf-8_*_

__author__ = 'Damon'

INVAILD_SYMBOL = r'\/:*?"<>|'

import os


def correct_name(words):
    '''
    判断添加的文字是否符合window重命名规则
    返回bool值
    '''
    name_bool = set(words).intersection(set(INVAILD_SYMBOL))
    return name_bool


def add_front(path, words):
    '''
    给文件添加前缀
    path：主文件夹路径
    words：添加的前缀文字
    '''
    for root, dirs, files in os.walk(path):
        n = 0  # 计数器
        for file in files:
            os.rename(os.path.join(root, file), os.path.join(root, words + file))
            n += 1
    print('给%d个文件添加了前缀.' % n)


def add_end(path, words):
    '''
    给文件添加后缀
    输入path：主文件夹路径
    输入words：添加的前缀文字
    '''
    for root, dirs, files in os.walk(path):
        n = 0  # 计数器
        for file in files:
            file_split = file.split('.')
            os.rename(os.path.join(root, file),
                      os.path.join(root, file_split[0] + words + '.' + file_split[-1]))
            n += 1
    print('给%d个文件添加了后缀.' % n)


def add_middle(path, words, index):
    pass


def change_indexname(path, words, index):
    pass

if __name__ == '__main__':
    while True:
        print('操作不能撤回！！！备份文件！')
        command = input('输入操作，增加前缀输入f；增加后缀输入e；退出输入q:')
        if command == 'q' or command == 'Q':
            break
        elif command == 'f' or command == 'F':
            path = input('输入文件夹路径或拖入文件夹(可以嵌套文件夹):')
            path = path.replace('"', '')
            while not os.path.isdir(path):
                print('文件夹路径错误')
                path = input('重新输入文件夹路径或拖入文件夹(可以嵌套文件夹):')
            words = input('输入要添加的字符:')
            while correct_name(words):
                print('包含非法字符')
                words = input('重新输入要添加的字符:')
            add_front(path, words)
        elif command == 'e' or command == 'E':
            path = input('输入文件夹路径或拖入文件夹(可以嵌套文件夹):')
            while not os.path.isdir(path):
                print('文件夹路径错误')
                path = input('重新输入文件夹路径或拖入文件夹(可以嵌套文件夹):')
            words = input('输入要添加的字符:')
            while correct_name(words):
                print('包含非法字符')
                words = input('重新输入要添加的字符:')
            add_end(path, words)
        elif command == 'q' or command == 'Q':
            break
        else:
            print('输入错误，重新输入!')

