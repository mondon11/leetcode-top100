#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 下午4:36
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0019removeNthFromEnd.py
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cnt = 0
        cur = head
        while(cur is not None):
            cnt = cnt + 1
            cur = cur.next

        cur = head
        if cnt - n == 0:
            head = head.next
        else:
            for i in range(cnt - n - 1):
                cur = cur.next
            cur.next = cur.next.next
        return head

    def removeNthFromEnd1(self, head, n):
        cnt = 0
        cur = head
        while(cur is not None):
            cnt = cnt + 1
            cur = cur.next

        dummy = ListNode(0,head)
        cur = dummy
        for i in range(cnt -n):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

    def removeNthFromEnd2(self, head, n):
        dummy = ListNode(0,head)
        start = dummy
        end = dummy
        for i in range(n):
            end = end.next
        while(end.next is not None):
            start = start.next
            end = end.next
        start.next = start.next.next
        return dummy.next

def genListNode(l):
    start = ListNode()
    cur = start
    for i in l:
        cur.next = ListNode(i)
        cur = cur.next
    return start.next

if __name__ == '__main__':
    sol = Solution()
    l = [1]
    n = 1
    listnode = genListNode(l)
    res = sol.removeNthFromEnd(listnode,n)
    print(1)