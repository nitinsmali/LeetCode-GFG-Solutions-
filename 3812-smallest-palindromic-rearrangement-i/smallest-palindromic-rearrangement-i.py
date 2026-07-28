class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        counts = Counter(s)

        mid_char = ""

        left_half = []
        for char in sorted(counts.keys()):
            if counts[char] % 2 != 0:
                mid_char = char

            left_half.append(char * (counts[char] // 2))

        left_str = "".join(left_half)        

        return left_str + mid_char + left_str[::-1]
