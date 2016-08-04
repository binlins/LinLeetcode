#148. Sort List
#-*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lnode = head
        nums = []
        while lnode is not None:
            nums.append(lnode.val)
            lnode = lnode.next
        nums.sort()
        i = 0
        nnode = head
        while nnode is not None:
            nnode.val = nums[i]
            i += 1
            nnode = nnode.next
        return head         #该解法不符合题目要求