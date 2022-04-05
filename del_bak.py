# -*-coding:utf-8-*-

"""删除文件夹下包括所有子目录的bak，dwl，tmp，lsp文件"""

__author__ = 'DamonLj'

import os


bak_nums = 0
dwl_nums = 0
tmp_nums = 0
lsp_nums = 0
dfile_size = 0


def del_bak(path):
    global bak_nums, bak_nums, dwl_nums, tmp_nums, lsp_nums, dfile_size

    for root, dirs, files in os.walk(path):
        for f in files:
            if f.split('.')[-1] == 'bak':
                dfile_size += os.path.getsize(os.path.join(root, f))
                os.remove(os.path.join(root, f))
                bak_nums += 1
            elif f.split('.')[-1] == 'dwl' or f.split('.')[-1] == 'dwl2':
                dfile_size += os.path.getsize(os.path.join(root, f))
                os.remove(os.path.join(root, f))
                dwl_nums += 1
            elif f.split('.')[-1] == 'tmp' or f.split('.')[-1] == 'fas':
                dfile_size += os.path.getsize(os.path.join(root, f))
                os.remove(os.path.join(root, f))
                tmp_nums += 1
            elif f.split('.')[-1] == 'lsp':
                dfile_size += os.path.getsize(os.path.join(root, f))
                os.remove(os.path.join(root, f))
                lsp_nums += 1


def size_format(size):
    if size < 1000:
        return '%i' % size + 'size'
    elif 1000 <= size < 1000000:
        return '%.1f' % float(size/1000) + 'KB'
    elif 1000000 <= size < 1000000000:
        return '%.1f' % float(size/1000000) + 'MB'
    else:
        return '%.1f' % float(size/1000000000) + 'GB'


if __name__ == '__main__':
    path = input('拖入文件夹或输入想要删除文件的目录（子文件夹会被清理）：')
    del_bak(path)
    print('删除了%d个bak文件，%d个dwl文件，%d个tmp文件, %d个lsp文件!\n' % (bak_nums, dwl_nums, tmp_nums, lsp_nums))
    print('一共删除了%s文件!\n' % size_format(dfile_size))
    input('enter键退出')
