#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 下午10:00
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0096numTrees.py
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            for j in range(0,i):
                dp[i] = dp[i] + dp[j]*dp[i-j-1]
        return dp[n]

if __name__ == '__main__':
    sol = Solution()
    print(sol.numTrees(3))