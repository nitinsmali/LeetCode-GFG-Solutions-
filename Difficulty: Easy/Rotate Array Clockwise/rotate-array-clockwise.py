class Solution:
    def rotateclockwise(self, arr, k):
        # code here
        n = len(arr)
        if n == 0:
            return
            
        k = k % n  # Handle cases where k >= n
        
        # Helper function to reverse a portion of the array
        def reverse(left, right):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
                
        # Step 1: Reverse the last k elements
        reverse(n - k, n - 1)
        # Step 2: Reverse the first n - k elements
        reverse(0, n - k - 1)
        # Step 3: Reverse the whole array
        reverse(0, n - 1)
