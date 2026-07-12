import pytest
from get_around import build_client_automatically

from diving_board import DivingBoard


@pytest.fixture(scope="session")
def client() -> DivingBoard:
    return DivingBoard(build_client_automatically())
