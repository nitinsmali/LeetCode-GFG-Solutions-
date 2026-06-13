class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """
        res = []
        for word in words:
            total_weight = sum(weights[ord(char) - ord('a')] for char in word)

            rem = total_weight % 26
            res.append(chr(ord('z') - rem))

        return ''.join(res)