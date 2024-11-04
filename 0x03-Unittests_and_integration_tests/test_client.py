#!/usr/bin/env python3
"""A module for testing the client module"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from typing import Dict
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """A class for testing the GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, url: str, mock_json):
        """A method for testing the org method"""
        test_client = GithubOrgClient(url)
        expected_url = f"https://api.github.com/orgs/{url}"
        mock_json.return_value = {
            "repo_url": f"https://api.github.com/orgs/{url}/repos"}
        result = test_client.org
        mock_json.assert_called_once_with(expected_url)
        self.assertEqual(result, {
            "repo_url": f"https://api.github.com/orgs/{url}/repos"})

    def test_public_repos_url(self):
        """Tests public_repos_url method"""
        test_payload = "https://api.github.com/orgs/google/repos"
        with patch(
          "client.GithubOrgClient.org", return_value=test_payload) as mock_url:
            result = mock_url()
            self.assertEqual(result, test_payload)

    @patch("client.get_json")
    def test_public_repos(self, mock_json):
        """Tests the public_repos method"""
        mock_json.return_value = {"id": "1", "name": "Ab"}
        value = mock_json("https://example.com")
        self.assertEqual(value, {"id": "1", "name": "Ab"})
        test_payload = {
                "license": {
                    "key": "apache"
                }
            }
        with patch(
          "client.GithubOrgClient._public_repos_url",
          return_value=test_payload) as mock_url:
            result = mock_url("apache")
            self.assertEqual(result, test_payload)
            mock_url.assert_called_once()
        mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, nested: Dict,
                         license: str, expected: bool) -> None:
        """Tests the has_license method"""
        test_client = GithubOrgClient("google")
        self.assertEqual(test_client.has_license(nested, license), expected)


@parameterized_class(("org_payload", "repos_payload",
                      "expected_repos", "apache2_repos"),
                     TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """A class for testing the GithubOrgClient service"""

    @classmethod
    def setUpClass(cls) -> None:
        """Class Setup for integration test"""
        cls.get_patcher = patch("requests.get")
        cls.mock = cls.get_patcher.start()
        cls.mock.side_effect = [
            {"json": lambda: cls.org_payload},
            {"json": lambda: cls.repos_payload}
        ]

    @classmethod
    def tearDownClass(cls) -> None:
        """Cleanup after Integration test"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Tests the public_repos method"""
        test_client = GithubOrgClient("org")
        self.assertEqual(test_client.org, self.org_payload)
        self.assertEqual(test_client.repos_payload, self.repos_payload)
        self.assertEqual(test_client.public_repos(), self.expected_repos)
        self.assertEqual(test_client.public_repos("License"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """Tests public repos with license argument"""
        test_client = GithubOrgClient("org")
        self.assertEqual(test_client.public_repos(), self.expected_repos)
        self.assertEqual(test_client.public_repos("License"), [])
        self.assertEqual(test_client.public_repos("apache-2.0"),
                         self.apache2_repos)
        self.mock.assert_called()
