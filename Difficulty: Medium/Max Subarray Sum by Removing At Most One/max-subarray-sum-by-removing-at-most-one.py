class Solution:
    def maxSumSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 1:
            return arr[0]
            
        # Initialize our trackers with the first element
        max_not_ignored = arr[0]
        max_ignored = arr[0]
        overall_max = arr[0]
        
        for i in range(1, n):
            # 1. Extend previous ignored path OR drop the current element completely
            current_ignored = max(max_ignored + arr[i], max_not_ignored)
            
            # 2. Standard Kadane's algorithm (no elements ignored yet)
            current_not_ignored = max(max_not_ignored + arr[i], arr[i])
            
            # Update trackers for the next iteration
            max_ignored = current_ignored
            max_not_ignored = current_not_ignored
            
            # Track the best global sum found
            overall_max = max(overall_max, max_ignored, max_not_ignored)
            
        return overall_max
