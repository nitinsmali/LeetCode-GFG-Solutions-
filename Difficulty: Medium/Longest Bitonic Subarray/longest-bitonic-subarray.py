class Solution:
	def bitonic(self,arr):
		# code here
		n = len(arr)
        if n == 0:
            return 0
            
        inc = [1] * n
        dec = [1] * n
        
        for i in range(1, n):
            if arr[i] >= arr[i - 1]:
                inc[i] = inc[i - 1] + 1
                
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[i + 1]:
                dec[i] = dec[i + 1] + 1
                
        max_len = 0
        for i in range(n):
            max_len = max(max_len, inc[i] + dec[i] - 1)
            
        return max_len