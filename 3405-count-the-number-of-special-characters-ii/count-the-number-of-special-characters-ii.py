class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        lastLower = [-1] * 26
        firstUpper = [float('inf')] * 26

        for i, ch in enumerate(word):
            if ch.islower():
                lastLower[ord(ch) - ord('a')] = i
            else:
                idx = ord(ch) - ord('A')
                firstUpper[idx] = min(firstUpper[idx], i)

        count = 0
        for i in range(26):
            if lastLower[i]!= -1 and firstUpper[i] != float('inf'):
                if lastLower[i] < firstUpper[i]:
                    count += 1
        return count 