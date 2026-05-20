class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        n = len(A)

        count = [0] * (n + 1)
        common = 0
        result = []

        for i in range(n):
            count[A[i]] += 1
            if count[A[i]] == 2:
                common += 1

            count[B[i]] += 1
            if count[B[i]] == 2:
                common += 1

            result.append(common)

        return result