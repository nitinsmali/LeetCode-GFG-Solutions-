class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        
        # Pre-apply modulo k to all array elements
        for i in range(n):
            nums[i] %= k

        # Segment tree arrays
        # tree_remain[cur] will hold a list of size k storing prefix frequencies
        tree_remain = [[0] * k for _ in range(4 * n)]
        tree_prod = [1] * (4 * n)

        def merge(left_idx: int, right_idx: int, parent_idx: int):
            # Calculate the total product of the combined range
            tree_prod[parent_idx] = (tree_prod[left_idx] * tree_prod[right_idx]) % k
            
            p_remain = tree_remain[parent_idx]
            l_remain = tree_remain[left_idx]
            r_remain = tree_remain[right_idx]
            l_prod = tree_prod[left_idx]
            
            # Reset parent remainders
            for i in range(k):
                p_remain[i] = 0

            # 1. Add prefixes that finish entirely within the left child range
            for i in range(k):
                p_remain[i] += l_remain[i]
                
            # 2. Add prefixes that cross over into the right child range
            # Scaled by the total cumulative product of the left child range
            for i in range(k):
                if r_remain[i] > 0:
                    target_rem = (l_prod * i) % k
                    p_remain[target_rem] += r_remain[i]

        def build(cur: int, left: int, right: int):
            if left == right:
                val = nums[left]
                tree_remain[cur][val] = 1
                tree_prod[cur] = val
                return
            
            mid = left + (right - left) // 2
            left_child = 2 * cur + 1
            right_child = 2 * cur + 2
            
            build(left_child, left, mid)
            build(right_child, mid + 1, right)
            merge(left_child, right_child, cur)

        def update(cur: int, left: int, right: int, idx: int, val: int):
            if left == right:
                # Reset previous frequencies
                for i in range(k):
                    tree_remain[cur][i] = 0
                tree_remain[cur][val] = 1
                tree_prod[cur] = val
                return
            
            mid = left + (right - left) // 2
            left_child = 2 * cur + 1
            right_child = 2 * cur + 2
            
            if idx <= mid:
                update(left_child, left, mid, idx, val)
            else:
                update(right_child, mid + 1, right, idx, val)
                
            merge(left_child, right_child, cur)

        def query_tree(cur: int, left: int, right: int, ql: int, qr: int) -> tuple[list[int], int]:
            # Returns a tuple: (remain_list, total_product)
            if ql <= left and right <= qr:
                return tree_remain[cur], tree_prod[cur]
            
            mid = left + (right - left) // 2
            left_child = 2 * cur + 1
            right_child = 2 * cur + 2
            
            if qr <= mid:
                return query_tree(left_child, left, mid, ql, qr)
            if ql > mid:
                return query_tree(right_child, mid + 1, right, ql, qr)
            
            # If the query range spans across both left and right branches, combine them manually
            l_rem, l_prod = query_tree(left_child, left, mid, ql, mid)
            r_rem, r_prod = query_tree(right_child, mid + 1, right, mid + 1, qr)
            
            combined_rem = [0] * k
            for i in range(k):
                combined_rem[i] += l_rem[i]
                
            for i in range(k):
                if r_rem[i] > 0:
                    target_rem = (l_prod * i) % k
                    combined_rem[target_rem] += r_rem[i]
                    
            combined_prod = (l_prod * r_prod) % k
            return combined_rem, combined_prod

        # Initialize the segment tree
        build(0, 0, n - 1)
        result = []
        
        # Process each persistent query
        for idx, val, start, x in queries:
            val %= k
            # Apply permanent point updates
            update(0, 0, n - 1, idx, val)
            
            # Bound check: If start is out of range, no prefix can be formed
            if start >= n:
                result.append(0)
            else:
                res_remain, _ = query_tree(0, 0, n - 1, start, n - 1)
                result.append(res_remain[x])
                
        return result
