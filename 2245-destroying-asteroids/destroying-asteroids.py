class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()

        curr_mass = mass

        for asteroid in asteroids:
            if curr_mass < asteroid:
                return False
            curr_mass += asteroid

        return True