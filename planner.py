from panel import Panel
from segmentation import PanelSegmenter
from rafters import RafterGrid, RafterOffsetFinder
from mounts import MountCalculator
from joints import JointCalculator
from models import MountingPlan
from exceptions import InvalidInputError

class MountingPlanner:
    """Service class for computing solar array mounts and joints."""

    def __init__(self):
        self.segmenter = PanelSegmenter()
        self.offset_finder = RafterOffsetFinder()
        self.mount_calculator = MountCalculator()
        self.joint_calculator = JointCalculator()

    def plan(self, panel_positions):
        """
        Compute the mounting plan for given panel positions.

        Args:
            panel_positions: List of dicts with keys "x" and "y" for the
                            top-left corner of each panel.

        Returns:
            MountingPlan with mounts and joints as lists of Points.

        Raises:
            InvalidInputError: If input has wrong structure or types.
            NoValidOffsetError: If no rafter offset satisfies constraints.
        """
        # 1. Walidacja
        self._validate_input(panel_positions)
        
        # 2. Edge case: pusta lista
        if not panel_positions:
            return MountingPlan(mounts=[], joints=[])
        
        # 3. Zbuduj panele
        panels = [Panel(item["x"], item["y"]) for item in panel_positions]
        
        # 4. Segmenty
        segments = self.segmenter.build_segments(panels)
        
        # 5. Offset i grid
        offset = self.offset_finder.find_offset(segments)
        grid = RafterGrid(offset)
        
        # 6. Mounty i jointy (niezależne)
        mounts = self.mount_calculator.calculate(segments, grid)
        joints = self.joint_calculator.calculate(panels)
        
        # 7. Zwróć MountingPlan
        return MountingPlan(mounts=mounts, joints=joints)

    def _validate_input(self, panel_positions):
        if not isinstance(panel_positions, list):
            raise InvalidInputError("Input must be a list.")
        
        for i, item in enumerate(panel_positions):
            if not isinstance(item, dict):
                raise InvalidInputError(f"Item {i} is not a dict.")
            if "x" not in item or "y" not in item:
                raise InvalidInputError(f"Item {i} is missing 'x' or 'y'.")
            
            for key in ("x", "y"):
                value = item[key]
                if isinstance(value, bool) or not isinstance(value, (int, float)):
                    raise InvalidInputError(f"Item {i}: '{key}' must be a number, got {type(value).__name__}.")