# Backend-Dev-Task

Computes mount positions (panel-to-rafter) and joint positions (panel-to-panel) for solar panel arrays. Given panel positions, returns where to attach the array to roof rafters and where to link panels.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Requires Python 3.10+.

## Usage

```python
from planner import MountingPlanner

panels = [{"x": 0, "y": 0}, {"x": 45.05, "y": 0}, ...]
plan = MountingPlanner().plan(panels)

print(plan.mounts)   # list of Points
print(plan.joints)   # list of Points
```

For the task example data (10 panels), returns 40 mounts and 12 joints.

## Tests

```bash
pytest tests/ -v
```

## Architecture

SOLID, single responsibility per class:

- `Panel` — geometry
- `PanelSegmenter` / `Segment` — groups touching panels per row
- `RafterGrid` — rafter positions for a given offset
- `RafterOffsetFinder` — finds valid offset; raises `NoValidOffsetError`
- `MountCalculator` — mounts on first/last in-zone rafter
- `JointCalculator` — joints at horizontal meetings, shifted for shared joints
- `MountingPlanner` — public service class, validates input, orchestrates

## Design decisions

Task description leaves several aspects open. Explicit choices:

- **Coordinates**: screen convention (y grows downward) — matches input data.
- **Mount Y**: two mounts per chosen rafter — panel's top and bottom edge.
- **Mount strategy**: first and last in-zone rafter (zone = `[left+2, right-2]`). Span ≤ 32 < 48 by construction. Strategy is swappable (Open/Closed).
- **Rafter offset**: not hardcoded — searched in `[0, 16)` with step 0.05. Returns first valid; raises if none works.
- **Segment**: panels in a row touching with gap < 1. Cantilever evaluated per segment (one row can have multiple segments).
- **Joints**: at horizontal meetings; shifted to vertical gap midpoint when an adjacent row panel is near (shared joint).
- **Empty input**: returns empty plan, not an error.
- **Float comparison**: `pytest.approx` with 0.01 tolerance in tests.