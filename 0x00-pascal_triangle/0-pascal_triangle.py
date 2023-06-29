#!/usr/bin/python3
'''
Pascal's Triangle
'''


def pascal_triangle(n):
    '''
    func: pascal_triangle
        returns a list of lists of integers
        representing the Pascal’s triangle of n
    args:
        <int: n> : number of rows (> 0)
    return:
        <list <of list>>
    '''
    triangle = []

    if n <= 0:
        return triangle

    triangle.append([1])

    for i in range(1, n):
        row = [1]

        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])

        row.append(1)
        triangle.append(row)

    return triangle
