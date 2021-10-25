import pytest
from model_bakery import baker

from retake.core.utils import ProcessData, PROCESS_01, PROCESS_02


@pytest.fixture
def process_data_01() -> ProcessData:
    return ProcessData(PROCESS_01)


@pytest.fixture
def process_data_02() -> ProcessData:
    return ProcessData(PROCESS_02)


@pytest.fixture
def process(db):
    parts_set = baker.prepare("core.Part", _quantity=3)
    return baker.make("core.Process", parts=parts_set)


@pytest.fixture
def part(db):
    return baker.make("core.Part")
