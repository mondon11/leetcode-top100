#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/23/21 4:36 AM
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0101isSymmetric.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(left,right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            return (left.val == right.val) and check(left.left, right.right) and check(left.right, right.left)

        return check(root,root)
