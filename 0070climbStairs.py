#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/16/21 6:34 AM
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0070climbStairs.py
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

if __name__ == '__main__':
    sol = Solution()
    res = sol.climbStairs(4)
    print(res)