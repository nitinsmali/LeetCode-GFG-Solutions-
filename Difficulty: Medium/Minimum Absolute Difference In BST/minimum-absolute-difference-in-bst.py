class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def absDiff(self, root):
        self.prev = None
        self.min_diff = float('inf')

        def in_order(node):
            if not node:
                return

            in_order(node.left)

            if self.prev is not None:
                self.min_diff = min(
                    self.min_diff,
                    node.data - self.prev
                )

            self.prev = node.data

            in_order(node.right)

        in_order(root)

        return self.min_diff