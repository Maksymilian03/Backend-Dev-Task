from rafters import RafterGrid


def test_rafter_grid():
    rafter = RafterGrid(10)

    assert rafter.rafters_in_range(2, 42.7)== [10, 26, 42]
    assert rafter.rafters_in_range(137.15, 177.85) == [138, 154, 170]
    assert rafter.rafters_in_range(11, 25) == []
    assert rafter.rafters_in_range(10, 10) == [10]