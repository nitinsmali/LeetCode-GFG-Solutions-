class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """

        # Calculate GCD without using math.gcd()
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Calculate LCM
        def lcm(a, b):
            return (a * b) // gcd(a, b)

        n = len(coins)

        # Store LCM of every subset
        subset_lcm = {}

        for mask in range(1, 1 << n):
            current_lcm = 1

            for i in range(n):
                if (mask >> i) & 1:
                    current_lcm = lcm(current_lcm, coins[i])

            subset_lcm[mask] = current_lcm

        # Count numbers <= target_val
        # that are divisible by at least one coin
        def count_multiples(target_val):
            total_count = 0

            for mask in range(1, 1 << n):
                bits = bin(mask).count('1')
                curr_lcm = subset_lcm[mask]

                if bits % 2 == 1:
                    total_count += target_val // curr_lcm
                else:
                    total_count -= target_val // curr_lcm

            return total_count

        # Binary search
        low = 1
        high = min(coins) * k

        while low < high:
            mid = (low + high) // 2

            if count_multiples(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low