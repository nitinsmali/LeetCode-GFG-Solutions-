class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)
        # Pair each element with its original index and sort by value
        sorted_pairs = sorted([(nums[i], i) for i in range(n)])
        
        result = [0] * n
        
        # Iterate through the sorted pairs to group elements
        i = 0
        while i < n:
            j = i + 1
            # Find the boundary of the current swappable group
            while j < n and sorted_pairs[j][0] - sorted_pairs[j - 1][0] <= limit:
                j += 1
            
            # Extract values and their original indices for the current group
            group_elements = sorted_pairs[i:j]
            
            # Sort the indices to place the smallest values into the leftmost positions
            indices = sorted([pair[1] for pair in group_elements])
            
            # Assign values to the sorted positions
            for k in range(len(group_elements)):
                result[indices[k]] = group_elements[k][0]
                
            # Move to the next group
            i = j
            
        return result