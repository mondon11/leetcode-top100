#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 下午5:33
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0020isValid.py
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        if len(s) <= 1:
            return False
        if s[0] == ')' or s[0] ==']' or s[0] =='}':
            return False
        l.append(s[0])
        for i in s[1:]:
            if i == '(' or i == '[' or i == '{':
                l.append(i)
            elif (i == ')' or i == ']' or i == '}') and len(l) == 0:
                return False
            elif l[-1] == '(' and i == ')':
                l.pop()
            elif l[-1] == '[' and i == ']':
                l.pop()
            elif l[-1] == '{' and i == '}':
                l.pop()
            else:
                return False
        if len(l) == 0:
            return True
        else:
            return False

    def isValid(self, s):
        if len(s) <= 1:
            return False
        l = []
        for i in s:
            l.append(i)
            if len(l) > 1:
                if (l[-1] == ')' and l[-2] == '(') or (l[-1] == ']' and l[-2] == '[') or (l[-1] == '}' and l[-2] == '{'):
                    l.pop()
                    l.pop()
        if len(l) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    s = "(){}}{"
    res = sol.isValid(s)
    print(res)
