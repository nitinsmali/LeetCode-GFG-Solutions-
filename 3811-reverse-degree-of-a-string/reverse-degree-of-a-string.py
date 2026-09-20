class Solution:
    def reverseDegree(self, s: str) -> int:
        total_degree = 0
    
        for index, char in enumerate(s, start=1):
            # Calculate position in reversed alphabet ('a'=26, 'b'=25, ..., 'z'=1)
            rev_alphabet_pos = 26 - (ord(char.lower()) - ord('a'))
            
            # Multiply by the 1-indexed position in the string
            total_degree += rev_alphabet_pos * index
            
        return total_degree
