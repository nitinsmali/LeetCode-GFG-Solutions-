class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
            
        max_num = max(nums)
        
        # Step 1: Count exact occurrences of each number in nums
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1
            
        # Step 2: Count how many numbers are multiples of each i
        multiples_count = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            for j in range(i, max_num + 1, i):
                multiples_count[i] += freq[j]
                
        # Step 3: Compute total pairs for each multiple and isolate exact GCD pairs
        gcd_counts = [0] * (max_num + 1)
        for i in range(max_num, 0, -1):
            c = multiples_count[i]
            # Combinations formula: n * (n - 1) / 2
            total_pairs = (c * (c - 1)) // 2
            
            # Subtract pairs that share a strictly larger GCD (multiples of i)
            subtracted_pairs = 0
            for j in range(2 * i, max_num + 1, i):
                subtracted_pairs += gcd_counts[j]
                
            gcd_counts[i] = total_pairs - subtracted_pairs
            
        # Step 4: Build prefix sums for binary searching the query indices
        prefix_sums = []
        gcd_values = []
        current_sum = 0
        
        for g in range(1, max_num + 1):
            if gcd_counts[g] > 0:
                current_sum += gcd_counts[g]
                prefix_sums.append(current_sum)
                gcd_values.append(g)
                
        # Step 5: Answer each query using binary search
        answer = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sums, q)
            answer.append(gcd_values[idx])
            
        return answer

        