class Panel:
    """
    A panel is a rectangular area defined by its top-left corner (x, y).
    Can calculate the coordinates of its corners and its left, right, top, and bottom edges.
    """
    WIDTH = 44.7
    HEIGHT = 71.1
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def corners(self):
        """
        Returns the coordinates of the corners of the panel.
        """
        left_top = (self.x, self.y)
        right_top = (self.x + self.WIDTH, self.y)
        right_bottom = (self.x + self.WIDTH, self.y + self.HEIGHT)
        left_bottom = (self.x, self.y + self.HEIGHT)
        return [
            left_top,
            right_top,
            right_bottom,
            left_bottom
        ]
    
    @property
    def left(self):
        """
        Returns the left edge of the panel.
        """
        return self.x
    
    @property
    def right(self):
        """
        Returns the right edge of the panel.
        """
        return self.x + self.WIDTH
    
    @property
    def top(self):
        """
        Returns the top edge of the panel.
        """
        return self.y
    
    @property
    def bottom(self):
        """
        Returns the bottom edge of the panel.
        """
        return self.y + self.HEIGHT
    
