from models import Point
from panel import Panel


class JointCalculator:
    """Calculates joint positions between adjacent solar panels."""

    DISTANCE_THRESHOLD = 1

    def calculate(self, panels: list[Panel]) -> list[Point]:
        """
        Compute joint positions for all horizontal panel meetings.

        For each pair of side-by-side panels in a row (gap < 1), creates
        a joint at the top and bottom edge of the meeting. If an adjacent
        row exists vertically (gap < 1) with a panel near the joint's x,
        the joint is shifted to the middle of the vertical gap (shared joint).

        Args:
            panels: List of Panel objects.

        Returns:
            List of joint center points.
        """
        joints = []

        rows = {}
        for panel in panels:
            rows.setdefault(panel.y, []).append(panel)

        sorted_ys = sorted(rows.keys())

        for y in sorted_ys:
            sorted_panels = sorted(rows[y], key=lambda panel: panel.x)
            for i in range(len(sorted_panels) - 1):
                left_panel = sorted_panels[i]
                right_panel = sorted_panels[i + 1]

                gap = right_panel.left - left_panel.right
                if not (0 <= gap < self.DISTANCE_THRESHOLD):
                    continue

                x_joint = (left_panel.right + right_panel.left) / 2
                y_top = self._maybe_merge_with_upper(
                    x_joint, left_panel.top, y, sorted_ys, rows
                )
                y_bottom = self._maybe_merge_with_lower(
                    x_joint, left_panel.bottom, y, sorted_ys, rows
                )
                joints.append(Point(x_joint, y_top))
                joints.append(Point(x_joint, y_bottom))
        return joints

    def _maybe_merge_with_lower(
        self,
        x_joint: float,
        y_bottom: float,
        y_current: float,
        sorted_ys: list[float],
        rows: dict,
    ) -> float:
        """Shift y_bottom to the middle of the vertical gap if a panel in the row below sits near x_joint."""
        for y_other in sorted_ys:
            if y_other <= y_current:
                continue
            gap = y_other - y_bottom
            if 0 <= gap < self.DISTANCE_THRESHOLD:
                if self._panel_near_x(rows[y_other], x_joint):
                    return (y_bottom + y_other) / 2
        return y_bottom

    def _maybe_merge_with_upper(
        self,
        x_joint: float,
        y_top: float,
        y_current: float,
        sorted_ys: list[float],
        rows: dict,
    ) -> float:
        """Shift y_top to the middle of the vertical gap if a panel in the row above sits near x_joint."""
        for y_other in sorted_ys:
            if y_other >= y_current:
                continue
            bottom_other = y_other + Panel.HEIGHT
            gap = y_top - bottom_other
            if 0 <= gap < self.DISTANCE_THRESHOLD:
                if self._panel_near_x(rows[y_other], x_joint):
                    return (bottom_other + y_top) / 2
        return y_top

    def _panel_near_x(self, row_panels: list[Panel], x_joint: float) -> bool:
        """Return True if any panel in the row has an edge or interior within DISTANCE_THRESHOLD of x_joint."""
        for panel in row_panels:
            if abs(panel.left - x_joint) < self.DISTANCE_THRESHOLD:
                return True
            if abs(panel.right - x_joint) < self.DISTANCE_THRESHOLD:
                return True
            if panel.left < x_joint < panel.right:
                return True
        return False
    