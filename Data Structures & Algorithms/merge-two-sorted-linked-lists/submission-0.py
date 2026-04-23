# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val <= list2.val :
                node.next = list1
                list1 = list1.next
            elif list2.val < list1.val :
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next =list1 or list2 # one of them is empty and thats why we got out of the while, if the second one is not empty we take the Non empty and push it into the new list

        return dummy.next
            
            

        