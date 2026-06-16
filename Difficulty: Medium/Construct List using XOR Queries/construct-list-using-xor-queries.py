class Solution:
    def constructList(self, queries):
        result = []
        cumulative_xor = 0
        
        # Process the queries list in reverse order (from end to beginning)
        for i in range(len(queries) - 1, -1, -1):
            query_type = queries[i][0]
            val = queries[i][1]
            
            if query_type == 1:
                # Accumulate the XOR value for elements present before this event
                cumulative_xor ^= val
            else:
                # Inserted elements only receive upcoming cumulative XOR changes
                result.append(val ^ cumulative_xor)
                
        # Handle the initial base element 0, which receives all XOR adjustments
        result.append(0 ^ cumulative_xor)
        
        # Sort the final collection as specified by the task constraints
        result.sort()
        return result
