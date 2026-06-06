class Solution:
    def lexicographicallySmallest(self, s, k):
        n = len(s)

        # Check if n is a power of 2
        if n > 0 and (n & (n - 1)) == 0:
            k //= 2
        else:
            k *= 2

        if k >= n:
            return "-1"

        stack = []

        for ch in s:
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        while k > 0:
            stack.pop()
            k -= 1

        return "".join(stack)