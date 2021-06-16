#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 下午9:26
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0053maxSubArray.py
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        max_val = nums[0]

        for i in range(len(nums)-1):
            val = nums[i]
            max_val = max(max_val, val)
            for j in range(i+1,len(nums)):
                val = val + nums[j]
                max_val = max(max_val,val)
        max_val = max(max_val,nums[-1])
        return max_val

    def maxSubArray1(self,nums):
        max_val = nums[0]
        pre = 0
        for i in range(len(nums)):
            pre = max(pre+nums[i], nums[i])
            max_val = max(max_val,pre)
        return max_val

if __name__ == '__main__':
    sol = Solution()
    res = sol.maxSubArray1([-2,1,-3,4,-1,2,1,-5,4])
    print(res)
