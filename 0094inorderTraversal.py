#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/21 下午9:13
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0094inorderTraversal.py
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root,res):
            if not root:
                return
            inorder(root.left,res)
            res.append(root.val)
            inorder(root.right,res)
        res = []
        inorder(root,res)
        return res