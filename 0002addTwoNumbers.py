#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 下午12:24
# @Author  : jt_hou
# @Email   : 949241101@qq.com
# @File    : 0002addTwoNumbers.py

class ListNode(object):
    def __init__(self,val = 0,next = None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        start = ListNode()
        cur = start
        while(l1 is not None and l2 is not None):
            cur.next = ListNode((l1.val + l2.val + carry) % 10)
            cur = cur.next
            carry = (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next

        while(l1 is not None):
            cur.next = ListNode((l1.val + carry) % 10)
            cur = cur.next
            carry = (l1.val + carry) // 10
            l1 = l1.next

        while (l2 is not None):
            cur.next = ListNode((l2.val + carry) % 10)
            cur = cur.next
            carry = (l2.val + carry) // 10
            l2 = l2.next

        if carry != 0:
            cur.next = ListNode(carry % 10)

        return start.next

    def addTwoNumbers1(self,l1,l2):
        start = ListNode()
        cur = start
        carry = 0
        while(l1 or l2 or carry):
            cur.next = ListNode((carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)) % 10)
            cur = cur.next
            carry = (carry + (l1.val if l1 else 0) + (l2.val if l2 else 0)) // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return start.next

def genListNode(l):
    start = ListNode()
    cur = start
    for i in l:
        cur.next = ListNode(i)
        cur = cur.next
    return start.next


if __name__ == '__main__':
    l1 = [9,9,9,9,9,9,9]
    l2 = [9,9,9,9]
    l1_node = genListNode(l1)
    l2_node = genListNode(l2)
    sol = Solution()
    res = sol.addTwoNumbers1(l1_node,l2_node)
    print(1)


