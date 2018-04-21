#!/user/bin/env python
#_*_coding:utf-8_*_


import os


class Node:
    def __init__(self, t ,l):
        self.t = t.replace('\n', '')  # 节点名字
        self.l = l  # 节点层级
        self.son = []  # 节点子节点列表
        self.full_path = ''  # 节点的完整路径


    def __repr__(self):
        return self.full_path


class Tree:
    def __init__(self):
        self.tree = []  # 类似os.walk返回的结构的树结构
        self.nodes = []  # 所有节点的完整路径
        # self.root = ''


    def mk_tree_from_txt(self, path, root=''):
        '''
        把缩进结构关系转化为类似[(root1,[dir1.1, dir1.2]), (root2,dir2)]结构
        '''
        root_node = Node(root, -1)  # 根节点
        root_node.full_path = root
        dp = [root_node]
        with open(path, 'r', encoding='utf-8') as f:
            for i in f.readlines():
                t = i.lstrip()
                l = len(i) - len(t)
                node = Node(t, l)
                self.nodes.append(node)
                while True:
                    if node.l > dp[0].l:
                        node.father = dp[0]
                        node.full_path = os.path.join(node.father.full_path, node.t)
                        dp[0].son.append(node)
                        # print(node.father.full_path, node.t)
                        break
                    else:
                        dp.pop(0)
                dp.insert(0, node)

        self.tree.append((root_node.full_path, [son.t for son in root_node.son]))
        for node in self.nodes:
            if node.son:
                self.tree.append((node.full_path, [son.t for son in node.son]))
        return self.tree


    def mk_dir_from_tree(self, root, tree):
        os.chdir(root)
        for root, dirs in tree:
            for dir in dirs:
                os.mkdir(os.path.join(root, dir))


if __name__ == "__main__":
    tree = Tree()
    tree.mk_tree_from_txt('tree.txt')
    print(tree.nodes)
    print(tree.tree)
    # root = input("输入创建文件夹的位置：")
    # mk_dir_from_tree(root, tree)

