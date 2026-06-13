from mounts import MountCalculator
from rafters import RafterOffsetFinder, RafterGrid
from segmentation import PanelSegmenter, Segment
from panel import Panel
from models import Point



def test_mounts_for_one_panel():
    panel = Panel(0, 0)
    segments = [Segment(panels=[panel])]
    grid = RafterGrid(10)
    points = MountCalculator().calculate(segments, grid)

    assert len(points) == 4
    assert Point(10, 0) in points
    assert Point(42, 71.1) in points


def test_mounts_for_panels_from_task_description():
    panels = [
        Panel(0, 0),
        Panel(45.05, 0),
        Panel(90.1, 0),
        Panel(0, 71.6),
        Panel(135.15, 0),
        Panel(135.15, 71.6),
        Panel(0, 143.2),
        Panel(45.05, 143.2),
        Panel(135.15, 143.2),
        Panel(90.1, 143.2)
    ]

    segments = PanelSegmenter().build_segments(panels)
    r = RafterOffsetFinder().find_offset(segments)
    grid = RafterGrid(r)
    points = MountCalculator().calculate(segments, grid)

    assert len(points) == 40


def test_mounts_for_panels():
    panels = [
        Panel(45.05, 0),
        Panel(90.1, 0),
        Panel(0, 71.6),
        Panel(135.15, 0),
        Panel(135.15, 71.6),
        Panel(0, 143.2),
        Panel(45.05, 143)]
    
    segments = PanelSegmenter().build_segments(panels)
    r = RafterOffsetFinder().find_offset(segments)
    grid = RafterGrid(r)
    points = MountCalculator().calculate(segments, grid)

    for segment in segments:
        xs_in_segment = [
        p.x for p in points
        if segment.left <= p.x <= segment.right
    ]
    assert min(xs_in_segment) <= segment.left + 16   # cantilever lewy
    assert max(xs_in_segment) >= segment.right - 16 

    unique = {(p.x, p.y) for p in points}
    assert len(unique) == len(points)