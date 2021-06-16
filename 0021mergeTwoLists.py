#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 下午9:06
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0021mergeTwoLists.py
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode()
        cur = res
        while(l1 is not None and l2 is not None):
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next
        '''
        while(l1 is not None):
            cur.next = ListNode(l1.val)
            cur = cur.next
            l1 = l1.next

        while(l2 is not None):
            cur.next = ListNode(l2.val)
            cur = cur.next
            l2 = l2.next
        '''
        if l1 is not None:
            cur.next = l1
        if l2 is not None:
            cur.next = l2

        return res.next

def genListNode(l):
    start = ListNode()
    cur = start
    for i in l:
        cur.next = ListNode(i)
        cur = cur.next
    return start.next

if __name__ == '__main__':
    sol = Solution()
    l1 = [1, 2, 4]
    l2 = [1, 3, 4]
    l1_node = genListNode(l1)
    l2_node = genListNode(l2)
    res = sol.mergeTwoLists(l1_node,l2_node)
    print(res)
