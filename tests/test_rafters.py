from rafters import RafterGrid, RafterOffsetFinder
from panel import Panel
from segmentation import Segment, PanelSegmenter



def test_rafter_grid():
    grid = RafterGrid(10)

    assert grid.rafters_in_range(2, 42.7)== [10, 26, 42]
    assert grid.rafters_in_range(137.15, 177.85) == [138, 154, 170]
    assert grid.rafters_in_range(11, 25) == []
    assert grid.rafters_in_range(10, 10) == [10]

def test_rafter_offset_finder():
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
    segmenter = PanelSegmenter()
    segments = segmenter.build_segments(panels)

    finder = RafterOffsetFinder(0.05)
    r = finder.find_offset(segments)
    grid = RafterGrid(r)
    for segment in segments:
        assert grid.rafters_in_range(segment.left+2, segment.left+16) != []
        assert grid.rafters_in_range(segment.right-16, segment.right-2) != []

    