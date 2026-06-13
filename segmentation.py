from dataclasses import dataclass


@dataclass
class Segment:
    """A contiguous run of panels in one row (sorted by x)."""

    panels: list

    @property
    def left(self) -> float:
        """X coordinate of the leftmost panel's left edge."""
        return self.panels[0].left

    @property
    def right(self) -> float:
        """X coordinate of the rightmost panel's right edge."""
        return self.panels[-1].right


class PanelSegmenter:
    """Groups panels into contiguous segments per row, split by horizontal gaps."""

    MAX_HORIZONTAL_GAP = 1

    def build_segments(self, panels) -> list[Segment]:
        """
        Group panels by row (same y), then split each row into contiguous
        segments wherever the horizontal gap between adjacent panels reaches
        MAX_HORIZONTAL_GAP.

        Args:
            panels: List of Panel objects.

        Returns:
            List of Segments, each containing panels sorted by x.
        """
        segments = []
        if not panels:
            return segments

        panels_by_y = {}
        for panel in panels:
            y = panel.top
            if y not in panels_by_y:
                panels_by_y[y] = []
            panels_by_y[y].append(panel)

        for y in sorted(panels_by_y.keys()):
            row = sorted(panels_by_y[y], key=lambda p: p.left)
            current_segment = [row[0]]
            for panel in row[1:]:
                if panel.left - current_segment[-1].right < self.MAX_HORIZONTAL_GAP:
                    current_segment.append(panel)
                else:
                    segments.append(Segment(current_segment))
                    current_segment = [panel]
            segments.append(Segment(current_segment))
        return segments
    