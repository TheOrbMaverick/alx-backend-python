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

        payload = [{"name": "google"}, {"name": "Twitter"}]
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
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that GithubOrgClient.has_license returns the correct value."""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integeration test for Fixtures """
    @classmethod
    def setUpClass(cls):
        """ Run setup before test """
        config = {"return_value.json.side_effect": [
            cls.org_payload, cls.repos_payload, cls.org_payload,
            cls.repos_payload,
        ]}
        cls.get_patch = patch('request.get', **config)
        cls.mock = cls.get_patch.start()

    def test_public_repo(self):
        """ Intergration test for public repo """
        class_test = GithubOrgClient('Google')

        self.assertEqual(class_test.org, self.org_payload)
        self.assertEqual(class_test.repos_payload, self.repos_payload)
        self.assertEqual(class_test.public_repos(), self.expected_repos)
        self.assertEqual(class_test.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ Intergration test for public repo with license """
        class_test = GithubOrgClient('google')

        self.assertEqual(class_test.public_repos(), self.expected_repos)
        self.assertEqual(class_test.public_repos("XLICENSE"), [])
        self.assertEqual(class_test.public_repos(
            "apache2_repos"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """ Run after test """
        cls.get_patch.stop()
