#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 上午11:40
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0001twoSum.py

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i,num in enumerate(nums):
            dict[num] = i
        for i,num in enumerate(nums):
            j = dict.get(target - num)
            if j is not None and j != i:
                return [i,j]


if __name__ == '__main__':
    sol = Solution()
    nums = [3,3,3]
    target = 6
    res = sol.twoSum(nums,target)
    print(res)