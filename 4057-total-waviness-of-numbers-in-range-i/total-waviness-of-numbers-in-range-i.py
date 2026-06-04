class Solution(object):
    def totalWaviness(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def waviness(num):
            s = str(num)

            if len(s) < 3:
                return 0

            count = 0

            for i in range(1, len(s) - 1):
                if (s[i] > s[i - 1] and s[i] > s[i + 1]) or \
                   (s[i] < s[i - 1] and s[i] < s[i + 1]):
                    count += 1

            return count

        ans = 0
        for num in range(num1, num2 + 1):
            ans += waviness(num)

        return ans
        