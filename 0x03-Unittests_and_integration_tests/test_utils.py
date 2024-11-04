#!/usr/bin/env python3
'''A module for testing the utils module'''
import unittest
from parameterized import parameterized
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Dict, Any


class TestAccessNestedMap(unittest.TestCase):
    '''A class for testing access_nested_map function'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested: Mapping,
                               sequence: Sequence, expected: Any) -> None:
        '''Tests access_nested_map'''
        self.assertEqual(access_nested_map(nested, sequence), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested: Mapping,
                                         sequence: Sequence,
                                         expected: Any) -> None:
        '''Tests access_nested_method's exceptions'''
        self.assertRaises(KeyError, access_nested_map, nested, sequence)


class TestGetJson(unittest.TestCase):
    '''A class for testing the get_json function'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        '''Tests the get_json method'''
        with patch('requests.get', return_value=test_payload) as mock_json:
            result = mock_json(input)
            self.assertEqual(result, test_payload)
            mock_json.assert_called_once_with(input)


class TestMemoize(unittest.TestCase):
    '''A class for testing the memoize decorator'''

    def test_memoize(self):
        '''Tests the memoize decorator'''

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test = TestClass()

        with patch.object(test, 'a_method', return_value=42) as mock_method:
            test.a_property
            test.a_property
            mock_method.assert_called_once()
