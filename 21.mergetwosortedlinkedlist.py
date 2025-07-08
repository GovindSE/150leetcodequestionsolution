# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        current= dummy

        while list1 and list2:
            val1= list1.val
            val2= list2.val
            if val1<=val2:
                current.next= ListNode(val1)
                current= current.next
                list1= list1.next
            elif val2<val1:
                current.next=ListNode(val2)
                current= current.next
                list2= list2.next
        while list1:
            current.next=ListNode(list1.val)
            current= current.next
            list1= list1.next
        while list2:
            current.next= ListNode(list2.val)
            current= current.next
            list2= list2.next
        return dummy.next

        
