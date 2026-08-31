# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Handled short lists safely
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        # Initialize trackers
        first_cp = -1
        prev_cp = -1
        min_dist = float('inf')
        
        prev = head
        curr = head.next
        idx = 1  # 0-indexed position tracker
        
        while curr.next:
            nxt = curr.next
            
            # Check if current node is a local maxima or local minima
            is_maxima = curr.val > prev.val and curr.val > nxt.val
            is_minima = curr.val < prev.val and curr.val < nxt.val
            
            if is_maxima or is_minima:
                if first_cp == -1:
                    # First critical point found
                    first_cp = idx
                else:
                    # Subsequent critical points: check and update min_dist
                    min_dist = min(min_dist, idx - prev_cp)
                    
                prev_cp = idx  # Update the last seen critical point
                
            # Move pointers forward
            prev = curr
            curr = nxt
            idx += 1

        # If fewer than two critical points were found
        if first_cp == prev_cp:
            return [-1, -1]
            
        max_dist = prev_cp - first_cp
        return [min_dist, max_dist]
