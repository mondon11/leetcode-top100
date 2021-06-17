#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/17/21 7:59 AM
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0461hammingDistance.py
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')

if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingDistance(1,4))