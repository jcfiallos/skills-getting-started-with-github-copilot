from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities


BASELINE_ACTIVITIES = deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset in-memory app state before each test."""
    activities.clear()
    activities.update(deepcopy(BASELINE_ACTIVITIES))
    yield
    activities.clear()
    activities.update(deepcopy(BASELINE_ACTIVITIES))


@pytest.fixture()
def client():
    return TestClient(app)
