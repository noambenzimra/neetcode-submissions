# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        root = head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #slow is now the middle

        head2 = self.reverseList(slow)
        slow.next = None  # <-- THIS CUTS THE LIST IN HALF
        self.connectInterleave(root, head2)
        



    

    def reverseList(self, head:Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        cur = head
        while cur :
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev



    def connectInterleave(self,head1:Optional[ListNode], head2:Optional[ListNode]) -> Optional[ListNode]:
        head = head1
        first = head1
        second = head2
        while first and second:
            tmp1 = first.next
            tmp2 = second.next
            
            # 2. Interleave the current nodes
            first.next = second    # 2 points to 8
            second.next = tmp1     # 8 points to 4
            
            # 3. Move the pointers forward for the next loop
            first = tmp1
            second = tmp2
        return head













