class SegmentTreeNode:
    def __init__(self, char=None):
        # If initialized with a single character (leaf node)
        if char is not None:
            self.max_len = 1
            self.pref_len = 1
            self.suff_len = 1
            self.left_char = char
            self.right_char = char
        else:
            self.max_len = 0
            self.pref_len = 0
            self.suff_len = 0
            self.left_char = ''
            self.right_char = ''

class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)
        # Segment tree array size allocation
        tree = [None] * (4 * n)
        
        def merge(left_node, right_node, left_size, right_size):
            """Merges two adjacent segment tree blocks."""
            parent = SegmentTreeNode()
            parent.left_char = left_node.left_char
            parent.right_char = right_node.right_char
            
            # Default tracking values
            parent.pref_len = left_node.pref_len
            parent.suff_len = right_node.suff_len
            
            # Maximum length is at least the max of either side
            parent.max_len = max(left_node.max_len, right_node.max_len)
            
            # Check if the boundary characters meet and can bridge together
            if left_node.right_char == right_node.left_char:
                combined_bridge = left_node.suff_len + right_node.pref_len
                parent.max_len = max(parent.max_len, combined_bridge)
                
                # Expand prefix if the left side is entirely uniform
                if left_node.pref_len == left_size:
                    parent.pref_len = left_size + right_node.pref_len
                    
                # Expand suffix if the right side is entirely uniform
                if right_node.suff_len == right_size:
                    parent.suff_len = right_size + left_node.suff_len
                    
            return parent

        def build(node, start, end):
            """Builds the initial segment tree from the string."""
            if start == end:
                tree[node] = SegmentTreeNode(s[start])
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1], mid - start + 1, end - mid)

        def update(node, start, end, idx, char):
            """Updates a character at a specific index."""
            if start == end:
                tree[node] = SegmentTreeNode(char)
                return
            mid = (start + end) // 2
            if start <= idx <= mid:
                update(2 * node, start, mid, idx, char)
            else:
                update(2 * node + 1, mid + 1, end, idx, char)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1], mid - start + 1, end - mid)

        # Step 1: Initialize the segment tree
        build(1, 0, n - 1)
        
        # Step 2: Process each update query sequentially
        ans = []
        for i in range(len(queryIndices)):
            idx = queryIndices[i]
            char = queryCharacters[i]
            update(1, 0, n - 1, idx, char)
            # tree[1] is the root node. It holds the answer for the entire string.
            ans.append(tree[1].max_len)
            
        return ans
