class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        last = [-1] * len(word2)
        i = len(word1) - 1
        j = len(word2) - 1
        
        # Step 1: Precompute last valid positions from the right
        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1
            
        ans = []
        can_skip = True
        j = 0
        
        # Step 2: Build the sequence greedily from the left
        for i, c in enumerate(word1):
            if j == len(word2):
                break
            if c == word2[j]:
                ans.append(i)
                j += 1
            elif can_skip and (j == len(word2) - 1 or i < last[j + 1]):
                can_skip = False
                ans.append(i)
                j += 1
                
        return ans if j == len(word2) else []
        