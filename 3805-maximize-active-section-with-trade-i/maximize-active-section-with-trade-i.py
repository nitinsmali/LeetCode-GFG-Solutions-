class Solution(object):
    def maxActiveSectionsAfterTrade(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_ones = s.count('1')
    
        max_zero_gain = 0
        prev_zero_len = float('-inf') # Start with -inf so a single leading '0' block cannot pair up prematurely
        
        # Linear scan to find consecutive segments
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '0':
                # Measure the length of the current '0' block
                curr_zero_len = 0
                while i < n and s[i] == '0':
                    curr_zero_len += 1
                    i += 1
                
                # Update the max gain from two adjacent '0' blocks
                max_zero_gain = max(max_zero_gain, prev_zero_len + curr_zero_len)
                prev_zero_len = curr_zero_len
            else:
                i += 1
                
        return total_ones + max(0, max_zero_gain)