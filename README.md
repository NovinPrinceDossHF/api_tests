| Test Case ID | Test Name | Validation | Type of Validation | Reasoning |
|:----------|:----------|:----------|:----------|:----------|
|Cat_Facts_001| test_get_single_fact_success| response.raise_for_status()|Error Handling / HTTP Status Code (implicit)| Automatically raises an HTTPError for 4xx (client error) or 5xx (server error) response status codes|
|Cat_Facts_001| test_get_single_fact_success| assert_status_code(response, 200) | HTTP Status Code | Fundamental check to ensure request was successfully processed |
|Cat_Facts_001| test_get_single_fact_success| assert_is_json(response) | Content Type / Response Format | Ensures that the response body is valid JSON |
|Cat_Facts_001| test_get_single_fact_success| assert isinstance(data, dict) | JSON Structure / Data Type |  APIs often return a JSON object (which maps to a Python dictionary) as their top-level structure for single entities. This confirms the expected overall structure |
|Cat_Facts_001| test_get_single_fact_success| assert expected_key in data | Content / Key Presence | This is a parameterized test that runs twice:It asserts that the fact key and length is present in the JSON response |
