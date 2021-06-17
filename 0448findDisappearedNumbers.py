#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/17/21 7:00 AM
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0448findDisappearedNumbers.py
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * (n + 1)
        rt = []
        for i in range(n):
            res[nums[i]] = 1
        for i in range(1,n+1):
            if res[i] == 0:
                rt.append(i)
        return rt

    def findDisappearedNumbers1(self, nums):
        dict = {}
        res = []
        for i in nums:
            dict[i] = 1
        for i in range(1,len(nums)+1):
            if dict.get(i) is None:
                res.append(i)
        return res

    def findDisappearedNumbers2(self, nums):
        n = len(nums)
        res = []
        for i in range(n):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] = -1 * nums[abs(nums[i]) - 1]
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.findDisappearedNumbers2([1,2,3,4,4]))