"""Main module for terminal-flag-banner package."""

from .flag_banner import display_single_flag_banner, generate_flag_list


def main():
    flag_list = generate_flag_list()
    for flag in flag_list:
        display_single_flag_banner(flag=flag, banner_length=4)


if __name__ == "__main__":
    main()
