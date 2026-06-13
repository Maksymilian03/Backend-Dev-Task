from dataclasses import dataclass


@dataclass
class Point:
    """
    Represents a 2D point in x-y coordinates.
    """
    x: float
    y: float


@dataclass
class MountingPlan:
    """Result of solar array mounting computation."""
    mounts: list[Point]
    joints: list[Point]