# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        before = dummy
        cur = head

        for i in range (left - 1):
            before = cur
            cur = cur.next

        prev = None
        for i in range (right - left + 1): #this is the window
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        # at the end of the loop for example for that input : 1->2->3->4->5, left = 2 , right = 4 we will get 1-> 2 ,4->3->2->None, 5->None , cur is at 5 and prev is at 4
        # so we have to connect before.next,next(this is exactly the next of 2 that is right now at None to cur, and before.next (this is exactly the head before the reversed in this example it is only 1,
        # we want it to points to 4 and this is exactly prev))
        
        before.next.next = cur
        before.next = prev

        return dummy.next    