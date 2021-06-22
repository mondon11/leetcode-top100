#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 下午2:01
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0064minPathSum.py
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for j in range(1,cols):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        for i in range(1,rows):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for i in range(1,rows):
            for j in range(1,cols):
                dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]





if __name__ == '__main__':
    sol = Solution()
    grid = [[7,4,8,7,9,3,7,5,0],[1,8,2,2,7,1,4,5,7],[4,6,4,7,7,4,8,2,1],[1,9,6,9,8,2,9,7,2],[5,5,7,5,8,7,9,1,4],[0,7,9,9,1,5,3,9,4]]
    res1 = sol.minPathSum(grid)
    print(res1)