# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        q = head
        pointer = q
        # Node = Listnode(q)
        
        while q != None:
            c= 0
            while q.val != 0:    
                c += q.val
                q = q.next
            
            pointer.val = c
            q = q.next
            pointer.next = q
            pointer = pointer.next
        return head
           
            
        