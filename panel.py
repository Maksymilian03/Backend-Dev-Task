class Panel:
    """A rectangular solar panel defined by its top-left corner."""

    WIDTH = 44.7
    HEIGHT = 71.1

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def corners(self) -> list[tuple[float, float]]:
        """Return the four corner coordinates in order: top-left, top-right, bottom-right, bottom-left."""
        left_top = (self.x, self.y)
        right_top = (self.x + self.WIDTH, self.y)
        right_bottom = (self.x + self.WIDTH, self.y + self.HEIGHT)
        left_bottom = (self.x, self.y + self.HEIGHT)
        return [left_top, right_top, right_bottom, left_bottom]

    @property
    def left(self) -> float:
        """X coordinate of the left edge."""
        return self.x

    @property
    def right(self) -> float:
        """X coordinate of the right edge."""
        return self.x + self.WIDTH

    @property
    def top(self) -> float:
        """Y coordinate of the top edge."""
        return self.y

    @property
    def bottom(self) -> float:
        """Y coordinate of the bottom edge."""
        return self.y + self.HEIGHT
    