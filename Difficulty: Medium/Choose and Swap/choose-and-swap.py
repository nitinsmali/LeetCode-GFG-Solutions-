class Solution:
    def chooseSwap(self, s: str) -> str:
        # Use a sorted list of unique characters for quick lookups
        chars_present = sorted(list(set(s)))
        
        for ch in s:
            # Check the smallest available unique character in the pool
            if chars_present and chars_present[0] < ch:
                smaller_ch = chars_present[0]
                
                # Perform the global swap for both characters
                s_list = list(s)
                for i in range(len(s_list)):
                    if s_list[i] == ch:
                        s_list[i] = smaller_ch
                    elif s_list[i] == smaller_ch:
                        s_list[i] = ch
                return "".join(s_list)
                
            # FIX: Only remove if it hasn't been removed by a previous duplicate
            if ch in chars_present:
                chars_present.remove(ch)
            
        return s
