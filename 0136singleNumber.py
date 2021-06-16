#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/16/21 7:02 AM
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0136singleNumber.py

from functools import reduce

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for k,v in enumerate(nums):
            if dict.get(v) is not None:
                dict.pop(v)
            else:
                dict[v] = k
        return list(dict.keys())[0]

    def singleNumber1(self, nums):
        return reduce(lambda x,y : x ^ y ,nums)

if __name__ == '__main__':
    sol = Solution()
    res = sol.singleNumber1([1,2,3,2,1])
    print(res)