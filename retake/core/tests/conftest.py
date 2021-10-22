import pytest

from retake.core.utils import ProcessData, PROCESS_01, PROCESS_02


@pytest.fixture
def process_01() -> ProcessData:
    return ProcessData(PROCESS_01)


@pytest.fixture
def process_02() -> ProcessData:
    return ProcessData(PROCESS_02)
