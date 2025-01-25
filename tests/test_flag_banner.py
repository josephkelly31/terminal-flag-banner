"""Tests for the flag_banner module"""

from terminal_flag_banner.flag_banner import TextBanner, generate_flag

japan_flag = generate_flag("JP")


def test_find_flag_column_length():
    """Test that the number of columns to display the flag in is calculated correctly"""
    length = TextBanner._find_flag_column_length(flag=japan_flag, needed_height=3)
    assert length == 10


def test_calculate_flag_height():
    """Test that the height of the flag is calculated correctly"""
    height = TextBanner._calculate_flag_height(flag=japan_flag, columns=10)
    assert height == 3


def test_find_banner_height():
    """Test that the height of the banner is calculated correctly"""
    height = TextBanner._find_banner_height(flag=japan_flag)
    assert height == 13
