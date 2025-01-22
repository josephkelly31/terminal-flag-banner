"""Tests for the flag_banner module"""

from terminal_flag_banner.flag_banner import TextBanner, generate_flag_list


def test_find_flag_column_length():
    """Test that the number of columns to display the flag in is calculated correctly"""
    flag_list = generate_flag_list()
    length = TextBanner._find_flag_column_length(flag=flag_list[0], needed_height=3)
    assert length == 10


def test_calculate_flag_height():
    """Test that the height of the flag is calculated correctly"""
    flag_list = generate_flag_list()
    height = TextBanner._calculate_flag_height(flag=flag_list[0], columns=10)
    assert height == 3


def test_find_banner_height():
    """Test that the height of the banner is calculated correctly"""
    flag_list = generate_flag_list()
    height = TextBanner._find_banner_height(flag=flag_list[0])
    assert height == 13
