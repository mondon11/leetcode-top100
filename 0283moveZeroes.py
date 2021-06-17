#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/17/21 6:33 AM
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0283moveZeroes.py
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        cnt = 0
        for i in nums:
            if i != 0:
                nums[cnt] = i
                cnt = cnt + 1
        for i in range(cnt,len(nums)):
            nums[i] = 0

    def moveZeroes1(self, nums):
        start = 0
        end = 0
        while end < len(nums):
            if nums[end] != 0:
                tmp = nums[start]
                nums[start] = nums[end]
                nums[end] = tmp
                start = start + 1
            end = end + 1



if __name__ == '__main__':
    sol = Solution()
    nums = [0,1,0,3,12]
    sol.moveZeroes1(nums)
    print(nums)

