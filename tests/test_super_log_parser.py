"""Tests for super-log-parser."""

import pytest
from super_log_parser import parser


class TestParser:
    """Test suite for parser."""

    def test_basic(self):
        """Test basic usage."""
        result = parser("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            parser("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = parser(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
