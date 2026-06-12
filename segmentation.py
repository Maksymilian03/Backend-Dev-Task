from dataclasses import dataclass


@dataclass
class Segment:
    """
    Represents a segment of panels.
    """
    panels: list

    @property
    def left(self):
        """
        Returns the left edge of the segment, which is the minimum left edge of its panels.
        """
        return self.panels[0].left
    
    @property
    def right(self):
        """
        Returns the right edge of the segment, which is the maximum right edge of its panels.
        """
        return self.panels[-1].right
    
    

class PanelSegmenter:
    """
    Segments panels into groups based on their horizontal proximity.
    """
    MAX_HORIZONTAL_GAP = 1

    def __init__(self):
        self.segments = []

    def build_segments(self, panels):
        """
        Segments the panels into groups based on their horizontal proximity.
        Panels that are within max_horizontal_gap of each other are grouped together.
        """
        
        if not panels:
            return self.segments
        panels_by_y = {}
        for panel in panels:
                y = panel.top
                if y not in panels_by_y:
                    panels_by_y[y] = []
                panels_by_y[y].append(panel)
            
        for y in sorted(panels_by_y.keys()):
            panels = sorted(panels_by_y[y], key=lambda panel: panel.left)
            current_segment = [panels[0]]
            for panel in panels[1:]:
                if panel.left - current_segment[-1].right < self.MAX_HORIZONTAL_GAP:
                    current_segment.append(panel)
                else:
                    self.segments.append(Segment(current_segment))
                    current_segment = [panel]
            self.segments.append(Segment(current_segment))
        return self.segments

