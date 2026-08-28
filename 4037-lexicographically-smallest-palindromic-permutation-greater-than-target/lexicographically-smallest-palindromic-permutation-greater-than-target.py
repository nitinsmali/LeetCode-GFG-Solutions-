class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
            
        odd_count = sum(1 for c in count if c % 2 != 0)
        if odd_count > (1 if n % 2 != 0 else 0):
            return ""
            
        mid_char = ""
        for i in range(26):
            if count[i] % 2 != 0:
                mid_char = chr(ord('a') + i)
                count[i] -= 1
                break
                
        half_len = n // 2
        
        def dfs(idx, tight, curr_half):
            if idx == half_len:
                full_str = curr_half + (mid_char if n % 2 != 0 else "") + curr_half[::-1]
                return full_str if full_str > target else ""
                
            start_ch = ord(target[idx]) - ord('a') if tight else 0
            for i in range(start_ch, 26):
                if count[i] >= 2:
                    count[i] -= 2
                    next_tight = tight and (i == ord(target[idx]) - ord('a'))
                    res = dfs(idx + 1, next_tight, curr_half + chr(ord('a') + i))
                    if res:
                        return res
                    count[i] += 2
            return ""
            
        return dfs(0, True, "")