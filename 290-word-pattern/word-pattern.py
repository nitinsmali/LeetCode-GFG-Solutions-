class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        return(
            len(pattern) == len(words) and
            len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))
        )
        