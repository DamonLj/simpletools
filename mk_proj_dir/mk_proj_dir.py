#!/user/bin/env python
#_*_coding:utf-8_*_


import os


def txt_to_tree(path):
    '''
    把缩进结构关系转化为类似[(root1,dir1), (root2,dir2)]关系
    '''
    tree = []
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if not lines[i].strip() or lines[i].strip().startswith('#'):
            continue
        elif lines[i].startswith(' ') or lines[i].startswith('\t'):
            line = lines[i].rstrip()
            
        else:
            pass
    return tree


def mk_dir_from_tree(root, tree):
    os.chdir(root)
    for root, dir in tree:
        os.mkdir(os.path.join(root, dir)


if __name__ == "__main__":
    path = 'tree.txt'
    tree = txt_to_tree(path)
    root = input("输入创建文件夹的位置：")
    mk_dir_from_tree(root, tree)

