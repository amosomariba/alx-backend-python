#!/usr/bin/env python3
"""Test client module for GithubOrgClient class.

This module contains unit tests for the GithubOrgClient class,
specifically testing the org method with mocked dependencies.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
import fixtures
import unittest.mock


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient functionality."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json) -> None:
        """Test that GithubOrgClient.org returns the correct value."""
        from client import GithubOrgClient

        expected_org_data = {"login": org_name, "id": 12345}
        mock_get_json.return_value = expected_org_data

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, expected_org_data)

    def test_public_repos_url(self) -> None:
        """Test that _public_repos_url returns expected URL."""
        from client import GithubOrgClient

        known_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
        }

        def org_property():
            return property(lambda self: known_payload)

        with patch('client.GithubOrgClient.org', new_callable=org_property):
            client = GithubOrgClient("google")
            result = client._public_repos_url
            self.assertEqual(result, known_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json) -> None:
        """Test that public_repos returns expected repository names."""
        from client import GithubOrgClient

        test_payload = [
            {"name": "episodes.dart"},
            {"name": "kratu"},
            {"name": "build_tools"},
        ]
        mock_get_json.return_value = test_payload

        test_url = "https://api.github.com/orgs/google/repos"
        property_patch = 'client.GithubOrgClient._public_repos_url'

        def property_factory():
            return property(lambda self: test_url)

        with patch(property_patch, new_callable=property_factory):
            client = GithubOrgClient("google")
            result = client.public_repos()
            expected = ["episodes.dart", "kratu", "build_tools"]
            self.assertEqual(result, expected)
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(
        self, repo: dict, license_key: str, expected: bool
    ) -> None:
        """Test that has_license returns expected boolean."""
        from client import GithubOrgClient

        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    fixtures.TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up mock responses using patch for requests.get."""
        def side_effect(url):
            mock_response = unittest.mock.Mock()
            if url == "https://api.github.com/orgs/google":
                mock_response.json.return_value = cls.org_payload
            elif url == cls.org_payload.get("repos_url"):
                mock_response.json.return_value = cls.repos_payload
            else:
                mock_response.json.return_value = {}
            return mock_response

        cls.get_patcher = patch('requests.get', side_effect=side_effect)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """Stop requests.get patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self) -> None:
        """Test that public_repos returns expected list from fixtures."""
        from client import GithubOrgClient

        client = GithubOrgClient("google")
        result = client.public_repos()
        self.assertEqual(result, self.expected_repos)

    def test_public_repos_with_license(self) -> None:
        """Test public_repos filtered by apache-2.0 license."""
        from client import GithubOrgClient

        client = GithubOrgClient("google")
        result = client.public_repos(license="apache-2.0")
        self.assertEqual(result, self.apache2_repos)

if __name__ == "__main__":
    unittest.main()
