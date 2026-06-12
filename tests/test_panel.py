from panel import Panel

def test_panel_points():
    panel = Panel(0, 0)
    points = panel.corners()
    assert points == [
        (0, 0),
        (44.7, 0),
        (44.7, 71.1),
        (0, 71.1)
    ]

def test_panel_points_with_offset():
    panel = Panel(45.05, 71.6)
    points = panel.corners()
    assert points == [
        (45.05, 71.6),
        (89.75, 71.6),
        (89.75, 142.7),
        (45.05, 142.7)
    ]

def test_panel_edges():
    panel = Panel(0, 0)
    assert panel.left == 0
    assert panel.right == 44.7
    assert panel.top == 0
    assert panel.bottom == 71.1