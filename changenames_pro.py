#!/user/bin/env python
#_*_coding:utf-8_*_

__author__ = 'Damon'

INVAILD_SYMBOL = r'\/:*?"<>|'

import os



def input_words():
    '''输入字符，并检查是否符合windows'''
    words = input('输入需要的字符（无字符则直接确认）:')
    while set(words).intersection(set(INVAILD_SYMBOL)):
        print('包含不允许的字符')
        words = input('重新输入需要的字符:')
    return words


def add_front(path, words):
    '''
    给文件添加前缀
    :param path：主文件夹路径
    :param words：添加的前缀文字
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
    :param path：主文件夹路径
    :param words：添加的前缀文字
    '''
    for root, dirs, files in os.walk(path):
        n = 0  # 计数器
        for file in files:
            file_split = file.split('.')
            os.rename(os.path.join(root, file),
                      ''.join([os.path.join(root, file_split[0]), words, '.', file_split[-1]]))
            n += 1
    print('给%d个文件添加了后缀.' % n)


def add_middle(path, words, index):
    '''
    在给定位置前添加字符
    :param path: 文件夹路径
    :param words: 字符
    :param index: 给定的位置
    '''
    for root, dirs, files in os.walk(path):
        n = 0  # 计数器
        for file in files:
            file_split = file.split('.')
            namelist = list(file_split[0])
            namelist.insert(index, words)
            newname = ''.join(namelist)
            os.rename(os.path.join(root, file),
                      ''.join([os.path.join(root, newname), '.', file_split[-1]]))
            n += 1
    print('给%d个文件插入了字符.' % n)


def change_indexname(path, words, index):
    '''
    替换指定位置的字符
    :param path: 文件夹路径
    :param words: 字符
    :param index: 给定的位置
    '''
    for root, dirs, files in os.walk(path):
        n = 0  # 计数器
        for file in files:
            file_split = file.split('.')
            namelist = list(file_split[0])
            namelist[index] = words
            newname = ''.join(namelist)
            os.rename(os.path.join(root, file),
                      ''.join([os.path.join(root, newname), '.', file_split[-1]]))
            n += 1
    print('给%d个文件更改了字符.' % n)


def replace_name(path, words, old_words):
    '''
    替换指定位置的字符
    :param path: 文件夹路径
    :param words: 字符
    :param old_words: 要替换的字符
    '''
    for root, dirs, files in os.walk(path):
        n = 0  # 计数器
        for file in files:
            file_split = file.split('.')
            newname = file_split[0].replace(old_words, words)
            os.rename(os.path.join(root, file),
                      ''.join([os.path.join(root, newname), '.', file_split[-1]]))
            n += 1
    print('给%d个文件替换了字符.' % n)


if __name__ == '__main__':
    while True:
        print('操作不能撤回！！！备份文件！')
        command = input('输入相应字母进行操作，按回车确认，无操作直接退出。\n增加前缀输入f；增加后缀输入e；替换字符输入r；\n'
                        '按位置插入字符输入m；按位置更改字符输入c;')
        if command == 'q' or command == 'Q':
            break
        else:
            path = input('输入文件夹路径或将文件夹拖入窗口:')
            path = path.replace('"', '')
            while not os.path.isdir(path):
                print('文件夹路径错误')
                path = input('重新输入文件夹路径或拖入文件夹:')
            if command == 'f' or command == 'F':
                words = input_words()
                add_front(path, words)
            elif command == 'e' or command == 'E':
                words = input_words()
                add_end(path, words)
            elif command == 'm' or command == 'M':
                index = input('要在第几个字符前插入(输入负数则倒数):')
                words = input_words()
                index = int(index)
                if index > 0:
                    index -= 1
                add_middle(path, words, index)
            elif command == 'c' or command == 'C':
                index = input('要替换第几个字符(输入负数则倒数):')
                words = input_words()
                index = int(index)
                if index > 0:
                    index -= 1
                change_indexname(path, words, index)
            elif command == 'r' or command == 'R':
                old_words = input('输入要被替换的字符（包含空格）:')
                words = input_words()
                replace_name(path, words, old_words)
            else:
                print('输入错误，重新输入!')
