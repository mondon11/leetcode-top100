#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/20 下午1:21
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0056merge.py
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key = lambda x : x[0])
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                if res[-1][1] <= interval[1]:
                    res[-1][1] = interval[1]
                else:
                    continue
        return res

if __name__ == '__main__':
    sol = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    res =sol.merge(intervals)
    print(res)