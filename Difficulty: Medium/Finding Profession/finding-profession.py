class Solution:
    def profession(self, level, pos):
        # code here
        flips = bin(pos - 1).count('1')


        if flips % 2 == 0:
            return "Engineer"
        return "Doctor"