"""Main module for terminal-flag-banner package."""

from .flag_banner import display_single_flag_banner, Flag

japan_flag = Flag(
    country_code="JP",
    country_name="Japan",
)

uk_flag = Flag(
    country_code="GB",
    country_name="United Kingdom",
)

spain_flag = Flag(
    country_code="ES",
    country_name="Spain",
)

flag_list = [japan_flag, uk_flag, spain_flag]


def main():
    for flag in flag_list:
        display_single_flag_banner(flag=flag, banner_length=4)


if __name__ == "__main__":
    main()
