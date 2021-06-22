#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 下午8:32
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0055canJump.py
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        max_reach = 0
        for i in range(n):
            if i <= max_reach:
                max_reach = max(max_reach,i+nums[i])
                if max_reach >= n-1:
                    return True
        return False

if __name__ == '__main__':
    sol = Solution()
    print(sol.canJump([1,1,0,2]))