#!/usr/bin/python3
'''Module that will return pascal triangle'''


def pascal_triangle(n):
    '''
    lists of integers representing the Pascal triangle
    '''
    lists = []
    if n == 0:
        return lists
    for k in range(n):
        lists.append([])
        lists[k].append(1)
        if (k > 0):
            for j in range(1, k):
                lists[k].append(lists[k - 1][j - 1] + lists[k - 1][j])
            lists[k].append(1)
    return lists
