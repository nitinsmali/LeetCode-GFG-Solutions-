class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0      # Tracks the maximum nesting depth found so her
        current_depth = 0  # Tracks the depth of the current position
        
        for char in s:
            if char == '(':
                current_depth += 1
                # Update max_depth if current_depth reaches a new peak
                max_depth = max(max_depth, current_depth)
            elif char == ')':
                current_depth -= 1
                
        return max_depth