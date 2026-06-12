import math

class RafterGrid:
    """
    Represents a grid of vertical rafters spaced evenly along the x-axis.
    """
    SPACING = 16

    def __init__(self, offset: float):
        """
        Args:
            offset: X coordinate of the first rafter.
        """
        self.offset = offset
        
    def rafters_in_range(self, start: float, end: float) -> list[float]:
        """
        Return x positions of all rafters within [start, end] (inclusive).

        Args:
            start: Left boundary of the range.
            end: Right boundary of the range.

        Returns:
            Sorted list of rafter x positions; empty if none fall in range.
        """
        list_of_rafters = []
      
        rafter_position = self.offset + math.ceil((start - self.offset) / self.SPACING) * self.SPACING 
        first_rafter = rafter_position
        
        i = 1
        while rafter_position <= end:
            list_of_rafters.append(rafter_position)
            rafter_position = first_rafter + i * self.SPACING
            i += 1
        return list_of_rafters
