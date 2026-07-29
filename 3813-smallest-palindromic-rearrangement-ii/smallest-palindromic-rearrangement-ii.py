class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        counts = Counter(s)
        odd_chars = [char for char, count in counts.items() if count % 2 != 0]

        if len(odd_chars) > 1:
            return ""

        mid = odd_chars[0] if odd_chars else ""
        half_counts = {char: count // 2 for char, count in counts.items() if count // 2 > 0}
        sorted_chars = sorted(half_counts.keys())
        half_len = sum(half_counts.values())
        
        total_perms = math.factorial(half_len)
        for count in half_counts.values():
            total_perms //= math.factorial(count)

        if total_perms < k:
            return ""

        first_half = []
        rem_len = half_len
        
        for _ in range(half_len):
            for char in sorted_chars:
                current_count = half_counts.get(char, 0)
                if current_count > 0:
                    next_perms = (total_perms * current_count) // rem_len
                    
                    if k <= next_perms:
                        first_half.append(char)
                        half_counts[char] -= 1
                        total_perms = next_perms
                        rem_len -= 1
                        break
                    else:
                        k -= next_perms
                        
        first_half_str = "".join(first_half)
        return first_half_str + mid + first_half_str[::-1]
        