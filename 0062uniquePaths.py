#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 下午1:49
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0062uniquePaths.py
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

if __name__ == '__main__':
    sol = Solution()
    res = sol.uniquePaths(3,7)
    print(res)