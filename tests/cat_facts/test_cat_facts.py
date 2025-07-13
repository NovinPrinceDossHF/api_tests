# tests/cat_facts/test_cat_facts.py
import pytest
from src.utils.helpers import assert_status_code, assert_is_json

class TestCatFactsAPI:

    @pytest.mark.parametrize("expected_key", ["fact", "length"])
    def test_get_single_fact_success(self, cat_facts_api_client, expected_key):
        response = cat_facts_api_client.get_single_fact()
        response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)

        assert_status_code(response, 200)
        assert_is_json(response)

        data = response.json()
        assert isinstance(data, dict), \
            f"Expected JSON response to be a dictionary, but got {type(data)}"
        assert expected_key in data, \
            f"Expected key '{expected_key}' not found in response: {data}"
        print(f"Successfully verified presence of key '{expected_key}'.")

    def test_fact_and_length_data_types(self, cat_facts_api_client):
        response = cat_facts_api_client.get_single_fact()
        response.raise_for_status()

        assert_status_code(response, 200)
        assert_is_json(response)

        data = response.json()

        assert "fact" in data, "Response missing 'fact' field."
        assert "length" in data, "Response missing 'length' field."

        assert isinstance(data["fact"], str), \
            f"Expected 'fact' to be a string, but got {type(data['fact'])}"
        assert isinstance(data["length"], int), \
            f"Expected 'length' to be an integer, but got {type(data['length'])}"
        print("Successfully verified 'fact' is string and 'length' is integer.")


    def test_fact_length_matches_content(self, cat_facts_api_client):
        response = cat_facts_api_client.get_single_fact()
        response.raise_for_status()

        assert_status_code(response, 200)
        assert_is_json(response)

        data = response.json()

        assert "fact" in data, "Response missing 'fact' field."
        assert "length" in data, "Response missing 'length' field."

        actual_fact_length = len(data["fact"])
        reported_length = data["length"]

        assert actual_fact_length == reported_length, \
            f"Fact length mismatch: Expected {actual_fact_length}, Got {reported_length}"
        print(f"Successfully verified fact length matches reported length ({actual_fact_length}).")

    def test_invalid_http_method(self, cat_facts_api_client):
        response = cat_facts_api_client.post_single_fact()
        assert_status_code(response, 405)
        print(f"Successfully verified 405 status code for POST request.")