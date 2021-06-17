#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/17/21 6:08 AM
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0169majorityElemen.py
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]
    def majorityElement1(self, nums):
        dict = {}
        for i in nums:
            if dict.get(i) is not None:
                dict[i] = dict[i]+1
            else:
                dict[i] = 1
            if dict[i] > len(nums)//2:
                return i

if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement1([1,2,1]))
    print(sol.majorityElement1([2,3,3,3]))