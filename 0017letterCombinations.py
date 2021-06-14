#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 下午1:47
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0017letterCombinations.py
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        dict = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        res = []
        s = []
        for digit in digits[0]:
            for i in dict[digit]:
                res.append(i)
        for digit in digits[1:]:
            for i in dict[digit]:
                for j in res:
                    s.append(j+i)
            res = s
            s =[]
        return res

    '''
    回溯算法框架：
    result = []
    def backtrack(路径, 选择列表):
        if 满足结束条件:
            result.add(路径)
            return

        for 选择 in 选择列表:
            #做选择
            将该选择从选择列表移除
            路径.add(选择)
            backtrack(路径, 选择列表)
            #撤销选择
            路径.remove(选择)
            将该选择再加入选择列表
    '''
    def letterCombinations1(self, digits):
        if len(digits) == 0:
            return []
        dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        res = []
        def backtrack(combinations,next_digit):
            if len(next_digit) == 0:
                res.append(combinations)
                return

            for letter in dict[next_digit[0]]:
                backtrack(combinations+letter, next_digit[1:])
        backtrack('',digits)
        return res


if __name__ == '__main__':
    sol = Solution()
    digits = "234"
    res = sol.letterCombinations1(digits)
    print(res)

