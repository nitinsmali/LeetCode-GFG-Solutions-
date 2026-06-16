class Solution:
    def isPalindrome(self, s):
        # code here
        left = 0
        right = len(s) - 1
        
        # Compare characters while moving towards the center
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True
