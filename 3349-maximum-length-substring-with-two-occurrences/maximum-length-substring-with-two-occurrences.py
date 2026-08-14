class Solution(object):
    def maximumLengthSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        max_len = 0
        counts = Counter()
    
        for right in range(len(s)):
            # Add the current character to the window
            counts[s[right]] += 1
            
            # If the count exceeds 2, shrink the window from the left
            while counts[s[right]] > 2:
                counts[s[left]] -= 1
                left += 1
                
            # Calculate the valid window size
            max_len = max(max_len, right - left + 1)
        
        return max_len