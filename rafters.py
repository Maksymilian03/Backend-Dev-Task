import math
from exceptions import NoValidOffsetError
from segmentation import Segment


class RafterGrid:
    """A grid of vertical rafters spaced evenly along the x-axis."""

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


class RafterOffsetFinder:
    """Finds a rafter grid offset that satisfies mounting constraints for all segments."""

    EDGE_CLEARANCE = 2
    MAX_CANTILEVER = 16

    def __init__(self, step: float = 0.05):
        """
        Args:
            step: Search resolution for the offset (in unit coordinates).
        """
        self.step = step

    def find_offset(self, segments: list[Segment]) -> float:
        """
        Find a rafter grid offset satisfying mounting constraints for all segments.

        Args:
            segments: Contiguous panel segments to validate against.

        Returns:
            The first offset in [0, 16) for which every segment has a rafter
            within both cantilever windows.

        Raises:
            NoValidOffsetError: If no offset satisfies the constraints.
        """
        for i in range(320):
            r = i * self.step
            grid = RafterGrid(r)
            if all(self._segment_ok(segment, grid) for segment in segments):
                return r
        raise NoValidOffsetError("No rafter offset in [0, 16) found.")

    def _segment_ok(self, segment: Segment, grid: RafterGrid) -> bool:
        """Return True if segment has a rafter in both cantilever windows."""
        return bool(
            grid.rafters_in_range(
                segment.left + self.EDGE_CLEARANCE,
                segment.left + self.MAX_CANTILEVER,
            )
            and grid.rafters_in_range(
                segment.right - self.MAX_CANTILEVER,
                segment.right - self.EDGE_CLEARANCE,
            )
        )
