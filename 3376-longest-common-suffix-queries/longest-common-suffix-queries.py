class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_idx = -1
        self.best_len = float('inf')
        
class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        """
        :type wordsContainer: List[str]
        :type wordsQuery: List[str]
        :rtype: List[int]
        """
        root = TrieNode()

        def update (node, word_len, idx):
            if word_len < node.best_len:
                node.best_len = word_len
                node.best_idx = idx

        for idx, word in enumerate(wordsContainer):
            node = root 
            update(node, len(word), idx)

            for ch in reversed(word):
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]
                update(node, len(word), idx)
        ans = []


        for query in wordsQuery:
            node = root

            for ch in reversed(query):
                if ch not in node.children:
                    break 
                node = node.children[ch]
            ans.append(node.best_idx)
        return ans