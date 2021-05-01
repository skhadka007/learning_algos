## Santosh Khadka
# www.LINK_HERE.com
'''
Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    pass

test_l1 = ListNode([1,2,4])
test_l2 = ListNode([1,3,4])

mergeTwoLists(test_l1, test_l2)