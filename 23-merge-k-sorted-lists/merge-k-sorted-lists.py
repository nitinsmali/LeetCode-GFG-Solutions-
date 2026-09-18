# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []
        counter = 0  # Prevents node comparison collisions when values are equal
        
        # Push the head of each list into the min-heap
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, counter, l))
                counter += 1
        
        dummy = ListNode(0)
        curr = dummy
        
        # Pop the smallest element and push its next element into the heap
        while heap:
            val, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1
                
        return dummy.next