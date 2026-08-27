class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        counts = Counter(s)
        
        # Helper to construct the smallest remaining suffix
        def get_smallest_suffix(cnts):
            res = []
            for char in sorted(cnts.keys()):
                if cnts[char] > 0:
                    res.append(char * cnts[char])
            return "".join(res)

        prefix = []
        best_ans = None
        
        # Step 1: Walk from left to right trying to match the target prefix
        for i in range(n):
            # Try to see if we can diverge at index 'i' by placing a character 
            # strictly greater than target[i]
            for c in sorted(counts.keys()):
                if c > target[i] and counts[c] > 0:
                    # Found a valid character to make it strictly greater
                    counts[c] -= 1
                    candidate = "".join(prefix) + c + get_smallest_suffix(counts)
                    counts[c] += 1
                    
                    # We want the earliest deviation or the one that minimizes the string
                    best_ans = candidate
                    break # The first one we find is the smallest possible for this position
            
            # Now, attempt to match target[i] exactly to keep exploring longer prefixes
            if counts[target[i]] > 0:
                counts[target[i]] -= 1
                prefix.append(target[i])
            else:
                # If we can't even match target[i], we cannot go deeper
                break
        else:
            # This block executes if the loop finished without breaking,
            # meaning we successfully matched the entire target string.
            # But the problem asks for STRICTLY GREATER, so an exact match is invalid.
            pass
            
        return best_ans if best_ans is not None else ""