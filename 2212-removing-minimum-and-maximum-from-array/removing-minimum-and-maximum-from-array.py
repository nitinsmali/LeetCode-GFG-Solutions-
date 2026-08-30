class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
    
        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))
        
        left_idx = min(min_idx, max_idx)
        right_idx = max(min_idx, max_idx)
        
        del_front = right_idx + 1
        del_back = n - left_idx
        del_both = (left_idx + 1) + (n - right_idx)
        
        # Step 4: Return the optimal solution
        return min(del_front, del_back, del_both)