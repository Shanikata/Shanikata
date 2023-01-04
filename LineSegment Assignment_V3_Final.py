# The getGroupedCoordinates method for the LineSegment class is designed 
# to return a list of collections of Coordinate objects representing points 
# along the line segment.

# The method takes three arguments:

# groupSize: The number of points to place in each collection.
# spacing: The spacing between points in the same collection.
# gap: The gap between collections.
# The method first calculates the difference in x and y between the 
# start and end points of the line segment. It then calculates the increment 
# in x and y for each point along the line segment based on the groupSize, 
# spacing, and gap values.

# Next, the method initializes an empty list to store the coordinates. 
# It then calculates the total number of groups that can be placed along the 
# line segment based on the spacing and gap values.

# Finally, the method iterates through the number of groups and calculates 
# the coordinates of each point in the group using the x_inc and y_inc values. 
# It appends each group of coordinates to the list and returns the list when 
# all groups have been processed.


from __future__ import annotations
from typing import List
import math


# Coordinate class: Takes 2 float values for x & y
class Coordinate:
    def __init__(self, x : float, y : float) -> None:
        self.X = x
        self.Y = y
        
    def DistanceTo(self, otherCoordinate : Coordinate):
        deltaX = otherCoordinate.X - self.X
        deltaY = otherCoordinate.Y - self.Y
        return math.sqrt(deltaX * deltaX + deltaY * deltaY)
    
    
#  LineSegment class; Takes 2 coordinates as start point & end point
class LineSegment:
    def __init__(self, startpoint : Coordinate, endpoint : Coordinate) -> None:
        self.StartPoint = startpoint
        self.EndPoint = endpoint
        self.Length = startpoint.DistanceTo(endpoint)

    def getGroupedCoordinates(self, groupSize: int, spacing: float, 
                              gap: float) -> List[List[Coordinate]]:
        """Returns a list of collections of coordinates along the line segment.
    
        Args:
            groupSize (int): The number of points to place in each collection.
            spacing (float): The spacing between points in the same collection.
            gap (float): The gap between collections.
        
        Returns:
            List[List[Coordinate]]: A list of lists of Coordinate objects representing the points along the line segment.
        """
        # Calculate the difference in x and y between the start and end points
        dx = self.EndPoint.X - self.StartPoint.X
        dy = self.EndPoint.Y - self.StartPoint.Y

        # Calculate the increment in x and y for each point along the line segment
        x_inc = (dx + gap) / (groupSize - 1)
        y_inc = (dy + gap) / (groupSize - 1)

        # Initialize a list to store the coordinates
        coordinates = []

        # Calculate the total number of groups that can be placed along the line segment
        num_groups = int((self.Length - spacing) / (spacing + gap))

        # Iterate through the number of groups and calculate the coordinates of each point
        for i in range(num_groups):
            group = []
            for j in range(groupSize):
                x = self.StartPoint.X + i * (spacing + gap) + j * x_inc
                y = self.StartPoint.Y + i * (spacing + gap) + j * y_inc
                group.append(Coordinate(x, y))
            coordinates.append(group)
    
        # Return the list of coordinates
        return coordinates


# Create a start point and an end point
startpoint = Coordinate(0, 0)
endpoint = Coordinate(10, 10)

# Create a line segment object
segment = LineSegment(startpoint, endpoint)

# Get the grouped coordinates along the line segment
coordinates = segment.getGroupedCoordinates(5, 2, 1)

# Print the grouped coordinates to the console
print(coordinates)
