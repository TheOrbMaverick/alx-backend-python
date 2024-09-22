#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class."""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.called_with_once(client.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """
        Test that GithubOrgClient._public_repos_url
        returns the correct value based on the given payload.
        """
        # Using the context manager to patch 'client.GithubOrgClient.org'
        with patch(
            'client.GithubOrgClient.org', new_callable=PropertyMock
                ) as mock_value:
            # Defining the mock payload for the org
            payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
            mock_value.return_value = payload

            # Create an instance of GithubOrgClient
            client = GithubOrgClient("google")
            # Fetch the _public_repos_url
            result = client._public_repos_url

            # Assert that the result matches the mocked payload
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that GithubOrgClient.public_repos returns the correct value."""
        payload = [{"name": "google"}, {"name": "twitter"}]
        mock_get_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url') as mock_public:
            mock_public.return_value = "What is happening!"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            intended = [load["name"] for load in payload]
            self.assertEqual(result, intended)

            mock_get_json.called_with_once()
            mock_public.called_with_once()

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

    @parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD)
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """ Integeration test for Fixtures """
        pass

#     @classmethod
#     def setUpClass(cls):
#         """Set up class method to mock requests.get for integration tests."""
#         cls.get_patcher = patch('requests.get')
#         cls.mock_get = cls.get_patcher.start()

#         def side_effect(url):
#             if url == (
#                     f"https://api.github.com/orgs/{cls.org_payload['login']}"
#                     ):
#                 return MockResponse(cls.org_payload)
#             elif url == cls.org_payload['repos_url']:
#                 return MockResponse(cls.repos_payload)
#             return MockResponse(None, 404)

#         cls.mock_get.side_effect = side_effect

#     @classmethod
#     def tearDownClass(cls):
#         """Tear down class method to stop the patcher."""
#         cls.get_patcher.stop()

#     def test_public_repos(self):
#         """Test GithubOrgClient.public_repos method."""
#         client = GithubOrgClient(self.org_payload['login'])
#         self.assertEqual(client.public_repos(), self.expected_repos)

#     def test_public_repos_with_license(self):
#         """Test GithubOrgClient.public_repos method with license filter."""
#         client = GithubOrgClient(self.org_payload['login'])
#         self.assertEqual(
#             client.public_repos(license="apache-2.0"), self.apache2_repos
#             )


# class MockResponse:
#     """Mock response object for requests.get."""
#     def __init__(self, json_data, status_code=200):
#         self.json_data = json_data
#         self.status_code = status_code

#     def json(self):
#         return self.json_data


# if __name__ == "__main__":
#     unittest.main()
