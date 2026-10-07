# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1, ptr2 = head.next, head
        while ptr1 and ptr1.next:
            if ptr1 == ptr2:
                return True
            ptr1 = ptr1.next.next
            ptr2 = ptr2.next
        return False
        
        
        # seen = set()
        # while head:
        #     if head in seen:
        #         return True
        #     seen.add(head)
        #     head = head.next
        # return False
        