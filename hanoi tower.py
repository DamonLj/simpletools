#!/user/bin/env python
# -*- coding: utf-8 -*-


def move(p1, p2):
    print('把%s移动到%s' % (p1, p2))


def hanoi(n, pA, pB, pC):
    '''把n个圆盘从pA移动到pC，另一个位置时pB'''
    if n > 1:
        hanoi(n - 1, pA, pC, pB)
        move(pA, pC)
        hanoi(n - 1, pB, pA, pC)
    else:
        move(pA, pC)


if __name__ == '__main__':
    hanoi(5, 'A', 'B', 'C')
