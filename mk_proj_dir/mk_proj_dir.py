#!/user/bin/env python
#_*_coding:utf-8_*_


import os


def txt_to_tree(path):
    tree = []
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if not lines[i].strip() or lines[i].strip().startswith('#'):
            continue
        elif lines[i].startswith(' ') or lines[i].startswith('\t'):
            pass
        else:
            pass
    return tree


def mk_dir_from_tree(tree):
    pass


if __name__ == "__main__":
    path = 'tree.txt'
    tree = txt_to_tree(path)
    mk_dir_from_tree(tree)

