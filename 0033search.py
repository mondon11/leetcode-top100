#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 下午5:46
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0033search.py
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

    def search1(self,nums,target):
        start = 0
        end = len(nums) - 1
        while(start <= end):
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]:
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1

if __name__ == '__main__':
    sol = Solution()
    print(sol.search1([4,5,6,0,1,2,3],5))