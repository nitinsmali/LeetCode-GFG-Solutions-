class Solution:
	def maxSubstring(self, s):
		# code here
		curr = 0
		ans  = -1
		for ch in s:
		    val = 1 if ch == "0" else -1
		    
		    curr = max(val, curr + val)
		    ans = max(ans, curr)
		    
		return ans