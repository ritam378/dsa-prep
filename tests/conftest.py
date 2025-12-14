"""
Pytest configuration and fixtures.
"""

import pytest
import sys
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


@pytest.fixture
def sample_array():
    """Sample array for testing."""
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sample_sorted_array():
    """Sample sorted array for testing."""
    return [1, 3, 5, 7, 9, 11]


@pytest.fixture
def sample_matrix():
    """Sample 2D matrix for testing."""
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
