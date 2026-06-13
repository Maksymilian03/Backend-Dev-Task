from dataclasses import dataclass


@dataclass
class Point:
    """A 2D point in x-y coordinates."""

    x: float
    y: float


@dataclass
class MountingPlan:
    """Result of a solar array mounting computation: mount and joint positions."""

    mounts: list[Point]
    joints: list[Point]