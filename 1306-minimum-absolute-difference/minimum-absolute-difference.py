class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()

        diff= float('inf')
        result=[]


        for i in range(1, len(arr)):
            diff= min(diff, arr[i]-arr[i-1])

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == diff:
                result.append([arr[i-1], arr[i]])

        return result 
                