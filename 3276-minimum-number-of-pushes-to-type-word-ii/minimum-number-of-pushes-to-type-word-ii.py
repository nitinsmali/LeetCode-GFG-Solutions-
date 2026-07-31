class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        frequencies = Counter(word).values()
    
    # 2. Sort frequencies in descending order
        sorted_frequencies = sorted(frequencies, reverse=True)
        
        total_pushes = 0
        
        # 3. Calculate pushes based on position
        for index, freq in enumerate(sorted_frequencies):
            # Every 8 characters, the number of required pushes increases by 1
            push_cost = (index // 8) + 1
            total_pushes += freq * push_cost
            
        return total_pushes
            
            