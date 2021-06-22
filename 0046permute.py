#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 下午7:05
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0046permute.py
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(nums,depth,size,used,path,res):
            if depth == size:
                res.append(path[:])
                return
            for i in range(size):
                if not used[i]:
                    path.append(nums[i])
                    used[i] = True
                    dfs(nums,depth+1,size,used,path,res)
                    used[i] = False
                    path.pop()
        size = len(nums)
        used = [False] * size
        res = []
        dfs(nums,0,size,used,[],res)
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([1,2,3]))
