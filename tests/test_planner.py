import pytest
from planner import MountingPlanner
from exceptions import InvalidInputError


PANELS_FROM_TASK = [
    {"x": 0, "y": 0},
    {"x": 45.05, "y": 0},
    {"x": 90.1, "y": 0},
    {"x": 0, "y": 71.6},
    {"x": 135.15, "y": 0},
    {"x": 135.15, "y": 71.6},
    {"x": 0, "y": 143.2},
    {"x": 45.05, "y": 143.2},
    {"x": 135.15, "y": 143.2},
    {"x": 90.1, "y": 143.2},
]


def test_plan_returns_correct_counts_for_task_data():
    planner = MountingPlanner()
    plan = planner.plan(PANELS_FROM_TASK)
    
    assert len(plan.mounts) == 40
    assert len(plan.joints) == 12


def test_plan_returns_empty_for_empty_input():
    planner = MountingPlanner()
    plan = planner.plan([])
    
    assert plan.mounts == []
    assert plan.joints == []


def test_plan_raises_on_non_list_input():
    planner = MountingPlanner()
    with pytest.raises(InvalidInputError):
        planner.plan("not a list")


def test_plan_raises_on_item_missing_x():
    planner = MountingPlanner()
    with pytest.raises(InvalidInputError):
        planner.plan([{"y": 0}])


def test_plan_raises_on_non_numeric_x():
    planner = MountingPlanner()
    with pytest.raises(InvalidInputError):
        planner.plan([{"x": "abc", "y": 0}])


def test_plan_raises_on_bool_as_number():
    planner = MountingPlanner()
    with pytest.raises(InvalidInputError):
        planner.plan([{"x": True, "y": 0}])