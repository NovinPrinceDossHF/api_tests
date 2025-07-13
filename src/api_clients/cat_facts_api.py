# src/api_clients/cat_facts_api.py
import requests
from config import settings

class CatFactsAPI:
    """
    Client for interacting with the Cat Facts API.
    Encapsulates API request logic.
    """
    def __init__(self):
        self.base_url = settings.BASE_URL

    def get_single_fact(self):
        """
        Sends a GET request to the /fact endpoint.
        Returns the requests.Response object.
        """
        url = f"{self.base_url}/fact"
        print(f"\nMaking GET request to: {url}")
        return requests.get(url)

    def post_single_fact(self):
        """
        Sends a POST request to the /fact endpoint (for testing unsupported methods).
        Returns the requests.Response object.
        """
        url = f"{self.base_url}/fact"
        print(f"\nMaking POST request to: {url}")
        return requests.post(url)