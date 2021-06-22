#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/19 下午7:41
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0039combinationSum.py
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(candidates,path,target,res):
            if target == sum(path) and sorted(path) not in res :
                res.append(sorted(path[:]))
                return
            if target < sum(path):
                return
            for i in candidates:
                if target > sum(path):
                    path.append(i)
                    dfs(candidates,path,target,res)
                    path.pop()
        res = []
        dfs(candidates,[],target,res)
        return res
    def combinationSum1(self, candidates, target):
        def dfs(candidates, begin, size, path, res, target):
            if target < 0:
                return
            if target == 0:
                res.append(path[:])
                return

            for index in range(begin, size):
                dfs(candidates, index, size, path + [candidates[index]], res, target - candidates[index])
                #path.append(candidates[index])
                #dfs(candidates,index,size,path,res,target-candidates[index])
                #path.pop()

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res


if __name__ == '__main__':
    sol = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(sol.combinationSum1(candidates,target))
