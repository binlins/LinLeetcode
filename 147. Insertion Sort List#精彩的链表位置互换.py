#147. Insertion Sort List
#-*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        cur = head
        while cur.next != None:
            if cur.next.val < cur.val:
                pre = dummy
                while pre.next.val < cur.next.val:
                    pre = pre.next
                temp = cur.next
                cur.next = temp.next    #将大小链表位置互换
                temp.next = pre.next
                pre.next = temp
            else:
                cur = cur.next
        return dummy.next
