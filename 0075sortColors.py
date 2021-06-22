#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 下午2:57
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0075sortColors.py
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i] = nums[p]
                nums[p] = 0
                p = p + 1
        for i in range(p,n):
            if nums[i] == 1:
                nums[i] = nums[p]
                nums[p] = 1
                p = p + 1

    def sortColors1(self,nums):
        p = 0
        q = len(nums) - 1
        i = 0
        while(i <= q):
            if nums[i] == 0:
                tmp = nums[p]
                nums[p] = 0
                nums[i] = tmp
                p = p + 1
                i = i + 1
            elif nums[i] == 1:
                i = i + 1
            else:
                tmp = nums[q]
                nums[q] = 2
                nums[i] = tmp
                q = q - 1

if __name__ == '__main__':
    sol = Solution()
    col = [2,0,2,1,1,0]
    sol.sortColors1(col)
    print(col)