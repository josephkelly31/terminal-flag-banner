"""Main module for terminal-flag-banner package."""

import argparse
from .flag_banner import TextBanner, generate_flag


def main():
    parser = argparse.ArgumentParser(
        description="Display a flag banner in the terminal."
    )
    parser.add_argument(
        "--country-code",
        type=str,
        required=True,
        help="The country code of the flag to display.",
    )
    args = parser.parse_args()

    flag = generate_flag(args.country_code.upper())
    if flag is None:
        print(f"Flag with country code '{args.country_code}' not found.")
        return
    banner = TextBanner()
    banner.display_text_banner(flag=flag)


if __name__ == "__main__":
    main()
