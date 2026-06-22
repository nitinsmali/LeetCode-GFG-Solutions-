class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counts = Counter(text)

        return min(
            counts['b'],
            counts['a'],
            counts['l'] // 2,
            counts['o'] //2,
            counts['n']
        )