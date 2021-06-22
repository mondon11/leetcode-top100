#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 下午4:27
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0048rotate.py
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        tmp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                tmp[j][n-i-1] = matrix[i][j]
        matrix[:] = tmp

if __name__ == '__main__':
    sol = Solution()
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sol.rotate(m)
    print(m)
