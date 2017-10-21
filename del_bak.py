# -*-coding:utf-8-*-

'''删除文件夹下包括所有子目录的bak，dwl，tmp文件'''

__author__ = 'DamonLj'

import os


path = input('拖入文件夹或输入想要删除文件的目录（子文件夹会被清理）：')
def del_bak(path):
    bak_nums = 0
    dwl_nums = 0
    tmp_nums = 0
    for root, dirs, files in os.walk(path):
        for f in files:
            if f.split('.')[-1] == 'bak':
                os.remove(os.path.join(root, f))
                bak_nums += 1
            elif f.split('.')[-1] == 'dwl' or f.split('.')[-1] == 'dwl2':
                os.remove(os.path.join(root, f))
                dwl_nums += 1
            elif f.split('.')[-1] == 'tmp' or f.split('.')[-1] == 'fas':
                os.remove(os.path.join(root, f))
                tmp_nums += 1
    print('删除了%d个bak文件，%d个dwl文件，%d个tmp文件' % (bak_nums, dwl_nums, tmp_nums))

if __name__ == '__main__':
    del_bak(path)
    input('enter键退出')
