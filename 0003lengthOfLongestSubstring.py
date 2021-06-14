#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 下午1:46
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0003lengthOfLongestSubstring.py
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        start = 0
        max_len = 0
        for cur,v in enumerate(s):
            if dict.get(v) is None:
                dict[v] = cur
            else:
                if dict.get(v) >= start:
                    start = dict.get(v) + 1
                dict[v] = cur
            max_len = max(max_len, (cur-start+1))
        return max_len

if __name__ == '__main__':
    sol = Solution()
    s = 'abba'
    res = sol.lengthOfLongestSubstring(s)
    print(1)







