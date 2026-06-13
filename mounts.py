from models import Point
from exceptions import NoValidOffsetError


class MountCalculator:
    """Calculates mount positions where panels attach to rafters."""

    def calculate(self, segments, grid) -> list[Point]:
        """
        Compute mount positions for all panels in the given segments.

        For each panel, selects the first and last rafter within its
        allowed zone (panel edges minus clearance) and places two mounts
        per rafter — one at the top edge and one at the bottom edge of
        the panel.

        Args:
            segments: Contiguous panel segments to process.
            grid: Rafter grid providing rafter positions in any range.

        Returns:
            List of mount points (top and bottom of each chosen rafter
            for each panel).

        Raises:
            NoValidOffsetError: If a panel has no rafter in its allowed zone.
        """
        points = []
        for segment in segments:
            for panel in segment.panels:
                rafters = grid.rafters_in_range(panel.left + 2, panel.right - 2)
                if not rafters:
                    raise NoValidOffsetError(
                        f"Panel at ({panel.x}, {panel.y}) has no rafter in its allowed zone."
                    )
                chosen = [rafters[0], rafters[-1]] if len(rafters) > 1 else [rafters[0]]
                for x in chosen:
                    points.append(Point(x, panel.top))
                    points.append(Point(x, panel.bottom))
        return points
    