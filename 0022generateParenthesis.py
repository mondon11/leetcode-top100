#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/15/21 8:15 AM
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0022generateParenthesis.py
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def isValid(s):
            if len(s) <= 1:
                return False
            l = []
            for i in s:
                l.append(i)
                if len(l) > 1:
                    if (l[-1] == ')' and l[-2] == '(') or (l[-1] == ']' and l[-2] == '[') or (
                            l[-1] == '}' and l[-2] == '{'):
                        l.pop()
                        l.pop()
            if len(l) == 0:
                return True
            else:
                return False

        res = ['']
        n = n*2
        while(n>0):
            store = []
            for combinations in res:
                store.append(combinations+'(')
                store.append(combinations+')')
            res = store
            n = n - 1
        rt = []
        for i in res:
            if isValid(i):
                rt.append(i)
        return rt



if __name__ == '__main__':
    sol = Solution()
    res = sol.generateParenthesis(3)
    print(res)

