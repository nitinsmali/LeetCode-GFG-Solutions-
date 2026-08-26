class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ones_indices = [i for i, ch in enumerate(s) if ch == '1']
    
        # If there are fewer than k '1's, no beautiful substring exists
        if len(ones_indices) < k:
            return ""
        
        min_len = float('inf')
        best_substring = ""
        
        # Slide a window of size k over the indices of '1's
        for i in range(len(ones_indices) - k + 1):
            start = ones_indices[i]
            end = ones_indices[i + k - 1]
            current_len = end - start + 1
            
            # Extract the candidate substring
            candidate = s[start:end + 1]
            
            # Update if a shorter length is found, or if it's the same length but lexicographically smaller
            if current_len < min_len:
                min_len = current_len
                best_substring = candidate
            elif current_len == min_len:
                if candidate < best_substring:
                    best_substring = candidate
                    
        return best_substring