#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 下午3:04
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0005longestPalindrome.py
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0

        for i in range(len(s)):
            l1 = self.expandAroundCenter(s,i,i)
            l2 = self.expandAroundCenter(s,i,i+1)
            maxLen = max(l1,l2)
            if maxLen >= end - start + 1:
                start = i - (maxLen-1)//2
                end = i + maxLen//2
        return s[start:end+1]

    def expandAroundCenter(self,s,left,right):
        while(left >=0 and right < len(s) and s[left] == s[right]):
            left = left - 1
            right = right +1
        return right-left+1-2

if __name__ == '__main__':
    sol = Solution()
    s = 'abbac'
    res = sol.longestPalindrome(s)
    print(res)

