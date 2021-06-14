#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 下午8:10
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0015threeSum.py
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_list = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        res = [nums[i],nums[j],nums[k]]
                        res = sorted(res)
                        if res not in res_list:
                            res_list.append(res)
                        break
        return res_list

    def threeSum1(self,nums):
        res_list = []
        dict = {}
        for k,v in enumerate(nums):
            dict[v] = k
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if dict.get(0-nums[i]-nums[j]) is not None:
                    if dict.get(0-nums[i]-nums[j]) > j:
                        res = [nums[i],nums[j],0-nums[i]-nums[j]]
                        res = sorted(res)
                        if res not in res_list:
                            res_list.append(res)
        return res_list

    def threeSum2(self,nums):
        res = []
        if len(nums) <=2 :
            return []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            start = i+1
            end = len(nums)-1
            while(start < end):
                if nums[i] + nums[start] + nums[end] == 0:
                    res.append([nums[i],nums[start],nums[end]])
                    start = start + 1
                    end = end - 1
                    while(start < end and nums[start - 1] == nums[start]):
                        start = start + 1
                    while(start < end and nums[end] == nums[end + 1]):
                        end = end - 1
                elif nums[i] + nums[start] + nums[end] > 0:
                    end = end - 1
                    while (start < end and nums[end] == nums[end + 1]):
                        end = end - 1
                else:
                    start = start + 1
                    while (start < end and nums[start - 1] == nums[start]):
                        start = start + 1
        return res





if __name__ == '__main__':
    sol = Solution()
    nums = [-1,0,1,2,-1,-4]
    res = sol.threeSum2(nums)
    print(res)