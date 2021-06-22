#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 下午2:54
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0034searchRange.py
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        end = -1
        cnt = 0
        if len(nums) == 0:
            return [-1,-1]
        for k,v in enumerate(nums):
            if v == target:
                end = k
                cnt = cnt + 1
            if v > target:
                break
        if end == -1:
            return [-1,-1]
        return [end-cnt+1,end]

    def searchRange1(self,nums,target):
        def binarySearch(nums,target,equal): # equal=1：寻找大于等于target的第一个index，equal=0：寻找大于target的第一个index
            ans = len(nums)
            left = 0
            right = len(nums) - 1

            while(left <= right):
                mid = (left + right) // 2
                if nums[mid] > target or (equal and nums[mid] >= target):
                    right = mid - 1
                    ans = mid
                else:
                    left = mid + 1
            return ans
        left = binarySearch(nums,target,1)
        right = binarySearch(nums,target,0)-1
        if(left <= right and nums[left] == target and nums[right] == target):
            return [left,right]
        return [-1,-1]

if __name__ == '__main__':
    sol = Solution()
    print(sol.searchRange1([5,7,7,8,8,10],8))
