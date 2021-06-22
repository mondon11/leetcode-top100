#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 下午7:42
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0078subsets.py
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            for j in res:
                tmp = j + [i]
                res = res + [tmp]
        return res

    def subsets1(self,nums):
        def backtrack(candidates,begin, path, size):
            res.append(path)
            for i in range(begin, size):
                backtrack(candidates, i + 1, path + [nums[i]],size)

        size = len(nums)
        res = []
        backtrack(nums, 0 ,[], size)
        return res


if __name__ == '__main__':
    sol = Solution()
    res = sol.subsets1([1,2,3])
    print(res)