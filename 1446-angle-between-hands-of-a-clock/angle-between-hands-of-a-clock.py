class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        h = hour % 12
        
        angle_hour = (30 * h) + (0.5 * minutes)
        angle_minutes = 6 * minutes

        diff = abs(angle_hour - angle_minutes)

        return min(diff, 360 - diff)


        