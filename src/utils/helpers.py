# src/utils/helpers.py

def validate_json_structure(data, expected_keys):
    """
    Helper to validate if a dictionary contains all expected keys.
    """
    for key in expected_keys:
        if key not in data:
            return False, f"Expected key '{key}' not found in response."
    return True, "All expected keys present."

def assert_status_code(response, expected_code):
    """
    Helper to assert the HTTP status code of a response.
    """
    assert response.status_code == expected_code, \
        f"Expected status code {expected_code}, but got {response.status_code}"

def assert_is_json(response):
    """
    Helper to assert if a response is valid JSON.
    """
    try:
        response.json()
    except ValueError:
        raise AssertionError("Response is not valid JSON.")