#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 下午3:59
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0011maxArea.py
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                h = min(height[i],height[j])
                l = j-i
                max_area = max(max_area,h*l)
        return max_area
    def maxArea1(self,height):
        max_area = 0
        left = 0
        right = len(height)-1
        while(right > left):
            max_area = max(max_area, (min(height[right], height[left])) * (right - left))
            if height[left] < height[right]:
                left = left + 1
            else:
                right = right - 1

        return max_area


if __name__ == '__main__':
    sol = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    res = sol.maxArea1(height)
    print(res)



