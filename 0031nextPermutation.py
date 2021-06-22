#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 下午5:18
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0031nextPermutation.py
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return
        i = len(nums)-2
        j = len(nums)-1
        k = len(nums)-1
        while(i>=0 and nums[i]>=nums[j]):
            i = i-1
            j = j-1
        if i >= 0:
            while(k>=j and nums[k]<=nums[i]):
                k = k-1
            tmp = nums[k]
            nums[k] = nums[i]
            nums[i] = tmp

        start = j
        end = len(nums)-1
        while(start<=end):
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            start = start + 1
            end = end - 1

if __name__ == '__main__':
    sol = Solution()
    nums = [2,3,1]
    sol.nextPermutation(nums)
    print(nums)


