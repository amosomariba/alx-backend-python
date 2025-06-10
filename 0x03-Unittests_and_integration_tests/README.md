# Unit and Integration Tests for GithubOrgClient

This directory contains unit and integration tests for the `GithubOrgClient` class, which interacts with the GitHub API to retrieve organization and repository information.

## Files

- **test_client.py**  
  Contains comprehensive unit and integration tests for the `GithubOrgClient` class, including:
  - Testing the `org` property with mocked API responses.
  - Verifying the `_public_repos_url` property.
  - Testing the `public_repos` method for correct repository name extraction.
  - Checking the `has_license` static method for license filtering.
  - Integration tests using fixture data to simulate real API responses.

- **fixtures.py**  
  Provides fixture data used in parameterized and integration tests.

## Features Tested

- Correct retrieval of organization data from the GitHub API.
- Extraction of the public repositories URL from organization data.
- Listing of public repositories for an organization.
- Filtering repositories by license type.
- Integration of all components with simulated HTTP responses.

## How to Run the Tests

1. **Install dependencies:**
   ```sh
   pip install parameterized

# Unit Tests for utils.py

This file contains unit tests for the utility functions defined in `utils.py`. The tests are written using Python's `unittest` framework and the `parameterized` library.

## Functions Tested

- **access_nested_map:**  
  Tests correct access to nested dictionaries using a sequence of keys, and verifies that `KeyError` is raised with the correct message for missing keys.

- **get_json:**  
  Tests that the function fetches JSON data from a URL using `requests.get` and returns the expected payload. HTTP requests are mocked to avoid real network calls.

- **memoize:**  
  Tests that the `memoize` decorator caches method results, ensuring the decorated method is only called once per instance.
