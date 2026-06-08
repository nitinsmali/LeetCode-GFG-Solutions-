class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def compute(self, head):
        if not head or not head.next:
            return head
            
        # Step 1: Reverse the linked list
        head = self.reverse(head)
        
        # Step 2: Traverse and remove nodes smaller than the max seen so far
        current = head
        max_node = head
        
        while current is not None and current.next is not None:
            if current.next.data < max_node.data:
                # Delete the next node as it is smaller than max_node
                current.next = current.next.next
            else:
                # Update current and the maximum node seen so far
                current = current.next
                max_node = current
                
        # Step 3: Reverse the list back to its original orientation
        return self.reverse(head)
        
    def reverse(self, head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
