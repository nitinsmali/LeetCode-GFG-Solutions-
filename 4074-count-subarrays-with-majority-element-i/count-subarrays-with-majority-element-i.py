class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        visited_prefixes = [0]
        
        current_prefix_sum = 0
        total_subarrays = 0
        
        for num in nums:
            current_prefix_sum += 1 if num == target else -1
            
            valid_count = bisect.bisect_left(visited_prefixes, current_prefix_sum)
            total_subarrays += valid_count
            
            bisect.insort(visited_prefixes, current_prefix_sum)
            
        return total_subarrays


        