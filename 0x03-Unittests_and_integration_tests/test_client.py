#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class."""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import fixtures


@parameterized_class([
    {
        "org_payload": fixtures.org_payload,
        "repos_payload": fixtures.repos_payload,
        "expected_repos": fixtures.expected_repos,
        "apache2_repos": fixtures.apache2_repos
    }
])
class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )
        self.assertEqual(result, test_payload)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that GithubOrgClient._public_repos_url
        returns the correct value.
        """
        test_payload = {
            "repos_url": "https://api.github.com/orgs/google/repos"
            }
        mock_org.return_value = test_payload

        client = GithubOrgClient("google")
        result = client._public_repos_url

        self.assertEqual(result, test_payload["repos_url"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"license": None}, "my_license", False),
        ({}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that GithubOrgClient.has_license returns the correct value."""
        client = GithubOrgClient("google")
        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)

    @classmethod
    def setUpClass(cls):
        """Set up class method to mock requests.get for integration tests."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            if url == (
                    f"https://api.github.com/orgs/{cls.org_payload['login']}"
                    ):
                return MockResponse(cls.org_payload)
            elif url == cls.org_payload['repos_url']:
                return MockResponse(cls.repos_payload)
            return MockResponse(None, 404)

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop the patcher."""
        cls.get_patcher.stop()


class MockResponse:
    """Mock response object for requests.get."""
    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data


if __name__ == "__main__":
    unittest.main()
