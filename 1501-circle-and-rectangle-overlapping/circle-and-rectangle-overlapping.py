class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))
        
        # Calculate the distance between the circle's center and this closest point
        distanceX = xCenter - closestX
        distanceY = yCenter - closestY
        
        # Check if the squared distance is less than or equal to the squared radius
        return (distanceX * distanceX + distanceY * distanceY) <= (radius * radius)