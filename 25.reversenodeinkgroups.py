# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=head
        count=0

        while curr:
            count+=1
            curr= curr.next

        
        dummy= ListNode(0)
        dummy.next=head
        prev= dummy

        while count>=k:
            curr= prev.next
            then= curr.next

            for _ in range(k-1):
                curr.next= then.next
                then.next=prev.next
                prev.next= then
                then= curr.next
            prev= curr
            count-=k
        return dummy.next
