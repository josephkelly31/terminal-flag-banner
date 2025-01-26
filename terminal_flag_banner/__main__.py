"""Main module for terminal-flag-banner package."""

import argparse
from .flag_banner import (
    TextBanner,
    generate_flag,
    display_flag_list_to_terminal,
    generate_random_country_code,
)


def main():
    parser = argparse.ArgumentParser(
        description="Display a flag banner in the terminal."
    )
    parser.add_argument(
        "--country-code",
        type=str,
        default=None,
        help="The country code of the flag to display.",
    )
    parser.add_argument(
        "--flag-list", action="store_true", help="List all available flags."
    )
    parser.add_argument(
        "--native-name",
        action="store_true",
        help="Display the name of the country in the country's native language.",
    )
    parser.add_argument(
        "--random-flag", action="store_true", help="Display a random flag."
    )

    args = parser.parse_args()

    if args.flag_list:
        print("Available flags:")
        display_flag_list_to_terminal()
        return

    if args.random_flag:
        random_country_code = generate_random_country_code()
        flag = generate_flag(random_country_code)
    else:
        flag = generate_flag(args.country_code.upper())
    if flag is None:
        print(f"Flag with country code '{args.country_code}' not found.")
        return
    banner = TextBanner()
    banner.display_text_banner(flag=flag, display_native_name=args.native_name)


if __name__ == "__main__":
    main()
