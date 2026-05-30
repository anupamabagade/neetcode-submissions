# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = node = ListNode() # dummy stays at the (beginning-1) but node is pushed through the linked list
        # Here value is 0 because default value of val is 0
        while list1 and list2: # Checks whethere a node exists or not
            if list1.val < list2.val :
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2 
                list2 = list2.next
            node = node.next

        node.next = list1 or list2 # When reached end of list1 or list2

        return dummy.next