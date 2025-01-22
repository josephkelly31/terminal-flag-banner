"""Main module for terminal-flag-banner package."""

from .flag_banner import TextBanner, Flag, generate_flag_list


def main():
    flag_list = generate_flag_list()
    for flag in flag_list:
        banner = TextBanner()
        banner.display_text_banner(flag=flag)


if __name__ == "__main__":
    main()
