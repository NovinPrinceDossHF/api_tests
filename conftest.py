import pytest
from src.api_clients.cat_facts_api import CatFactsAPI

@pytest.fixture(scope="session")
def cat_facts_api_client():
    """
    Provides a session-scoped instance of the CatFactsAPI client.
    """
    return CatFactsAPI()