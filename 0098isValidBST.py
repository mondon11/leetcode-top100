#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 下午10:30
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0098isValidBST.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    pre = -float('inf')
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def inorder(root):
            if root is None:
                return True
            l = inorder(root.left)
            if self.pre < root.val:
                self.pre = root.val
            else:
                return False
            r = inorder(root.right)
            return (l and r)


        return inorder(root)