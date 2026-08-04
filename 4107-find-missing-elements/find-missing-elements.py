class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        # Step 1: Find the bounds of the original range
        min_val = min(nums)
        max_val = max(nums)
        
        # Step 2: Store unique integers in a set for O(1) lookups
        num_set = set(nums)
        
        # Step 3: Collect all integers missing from the range
        missing_numbers = []
        for x in range(min_val, max_val + 1):
            if x not in num_set:
                missing_numbers.append(x)
                
        return missing_numbers
