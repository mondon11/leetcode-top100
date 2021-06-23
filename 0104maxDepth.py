#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/23/21 7:21 AM
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0104maxDepth.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        return max(left_max,right_max)+1