#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/16/21 6:04 AM
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0121maxProfit.py
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_price = 0
        for i in range(len(prices)-1):
            price = 0
            for j in range(i+1,len(prices)):
                price = max(price, prices[j] - prices[i])
            max_price = max(max_price,price)
        return max_price

    def maxProfit1(self, prices):
        max_profit = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            max_profit = max(max_profit,prices[i]-min_price)
            if prices[i] < min_price:
                min_price = prices[i]
        return max_profit

if __name__ == '__main__':
    sol = Solution()
    res = sol.maxProfit1([7, 1, 5, 3, 6, 4])
    print(res)