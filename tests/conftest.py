import copy

import pytest
from fastapi.testclient import TestClient

from src import app as app_module

_INITIAL_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Arrange: reset in-memory activities before each test."""
    app_module.activities = copy.deepcopy(_INITIAL_ACTIVITIES)


@pytest.fixture
def client():
    """Arrange: provide a FastAPI test client."""
    return TestClient(app_module.app)
