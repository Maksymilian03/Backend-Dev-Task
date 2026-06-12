import pytest

from segmentation import PanelSegmenter
from panel import Panel

def test_segmentation():
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
    assert len(segments) == 4
    assert segments[0].left == 0
    assert segments[0].right == pytest.approx(179.85)
    assert segments[1].left == 0
    assert segments[1].right == pytest.approx(44.7)
    assert segments[2].left == pytest.approx(135.15)
    assert segments[2].right == pytest.approx(179.85)
    assert segments[3].left == 0
    assert segments[3].right == pytest.approx(179.85)
    