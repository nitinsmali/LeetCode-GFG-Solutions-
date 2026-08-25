# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        # Loop while there are nodes to process or a carry left over
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum for the current position
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            
            # Create new node with the single-digit remainder
            curr.next = ListNode(total_sum % 10)
            curr = curr.next
            
            # Move to the next nodes if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        return dummy.next
        