from joints import JointCalculator
from panel import Panel
from models import Point
import pytest



def test_joints_for_panels_from_task():
    panels = [Panel(0,0), Panel(45.05,0), Panel(90.1,0), Panel(135.15,0),
              Panel(0,71.6), Panel(135.15,71.6),
              Panel(0,143.2), Panel(45.05,143.2), Panel(90.1,143.2), Panel(135.15,143.2)]
    
    expected = [
        Point(44.875, 0), Point(89.925, 0), Point(134.975, 0),
        Point(44.875, 71.35), Point(89.925, 71.1), Point(134.975, 71.35),
        Point(44.875, 142.95), Point(89.925, 143.2), Point(134.975, 142.95),
        Point(44.875, 214.3), Point(89.925, 214.3), Point(134.975, 214.3),
    ]
    
    joints = JointCalculator().calculate(panels)
    
    assert len(joints) == 12
    

    actual_sorted = sorted(joints, key=lambda p: (p.y, p.x))
    expected_sorted = sorted(expected, key=lambda p: (p.y, p.x))
    
    for a, e in zip(actual_sorted, expected_sorted):
        assert a.x == pytest.approx(e.x, abs=0.01)
        assert a.y == pytest.approx(e.y, abs=0.01)