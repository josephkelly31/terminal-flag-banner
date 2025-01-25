"""Python module to display a banner of flags in the terminal
"""

import art
import csv
from dataclasses import dataclass
import os

from importlib import resources
from PIL import Image
import ascii_magic
from . import data


@dataclass
class Flag:
    """Class to represent a flag"""

    country_code: str = None
    country_name: str = None
    flag_image_file_exists: bool = False
    flag_image: Image = None

    def __post_init__(self):
        flag_image_file_path = f"{self.country_code}.png"
        my_resources = resources.files(data)
        path = my_resources / flag_image_file_path
        self.flag_image_file_exists = os.path.exists(path)
        self.flag_image = Image.open(path)


class Banner:

    @classmethod
    def flag_to_text(cls, flag: Flag, columns: int) -> str:
        """Generates an image of a flag as a string

        Args:
            flag (Flag): The flag object to generate the string from
            columns (int): The number of columns to display the flag in

        Returns:
            str: The string representing the flag
        """
        if flag.flag_image is None:
            print("Image is None!")
            return False

        my_art = ascii_magic.from_pillow_image(flag.flag_image)
        return my_art.to_ascii(columns=columns)

    def display_flag(self, flag: Flag) -> bool:
        """Function to display a flag to a terminal

        Args:
            flag (Flag): the Flag object to display to the terminal

        Returns:
            bool: whether the flag is displayed (whether exists in the package's flag folder)
        """
        if not flag.flag_image_file_exists:
            print(
                f"Country: {flag.country_name} ({flag.country_code}) has no flag image!"
            )
            return False

        self._display_img(flag.flag_image)
        return True

    def _display_img(self, image: Image) -> bool:
        """
        Displays an image on the terminal.

        Args:
            image (Image): The image object to display to the terminal.

        Returns:
            bool: True if the image was successfully displayed, False otherwise.
        """
        if image is None:
            print("Image is None!")
            return False

        my_art = ascii_magic.from_pillow_image(image)
        my_art.to_terminal()
        return True

    def generate_banner_img(self, flags: list[Flag]) -> Image:
        """Generates a banner image from a list of Flag objects

        Args:
            flags (list[Flag]): The flags to make the banner out of

        Returns:
            Image: The banner image
        """
        if len(flags) == 0:
            return None

        banner_img = flags[0].flag_image

        for flag in flags[1:]:
            banner_img = extend_banner(
                banner_img=banner_img, flag_to_append=flag.flag_image
            )

        return banner_img

    def display_single_flag_banner(self, flag: Flag, banner_length: int) -> bool:
        """Function to display a banner made up of a single flag to a terminal

        Args:
            flag (Flag): the Flag object to display to the terminal
            banner_length (int): the number of flags that make up the banner

        Returns:
            bool: whether the flag is displayed (whether exists in the package's flag folder)
        """
        if not flag.flag_image_file_exists:
            print(
                f"Country: {flag.country_name} ({flag.country_code}) has no flag image!"
            )
            return False

        single_flag_banner = self.generate_banner_img(
            flags=[flag for _ in range(banner_length)]
        )
        self._display_img(image=single_flag_banner)
        return True


def extend_banner(banner_img: Image, flag_to_append: Image) -> Image:
    """Adds an image to the right of another image, creating a banner of images

    Args:
        banner_img (Image): The banner to append to
        flag_to_append (Image): The flag to append to the banner

    Returns:
        Image: The appended banner
    """
    if banner_img is None and flag_to_append is None:
        print("Banner image and appending image are both None!")
        return None

    if banner_img is None:
        return flag_to_append

    if flag_to_append is None:
        return banner_img

    extended_banner_img = Image.new(
        "RGB", (banner_img.width + flag_to_append.width, banner_img.height)
    )
    extended_banner_img.paste(banner_img, (0, 0))
    extended_banner_img.paste(flag_to_append, (banner_img.width, 0))
    return extended_banner_img


class TextBanner(Banner):

    def __new__(cls):
        return super().__new__(cls)

    @classmethod
    def _generate_country_name(cls, flag: Flag) -> str:
        """Generates a string representing the country name and country code

        Args:
            flag (Flag): The flag object to generate the string from

        Returns:
            str: The string representing the country name and country code
        """
        country_string = f"{flag.country_name}"
        country_name_art = art.text2art(country_string, font="block")
        country_name_art = cls._pad_country_name(country_name=country_name_art)
        return country_name_art

    @staticmethod
    def _generate_country_name_padding(country_name_art: str) -> str:
        """Generates padding for the country name

        Args:
            country_name_art (str): the country name to generate padding for

        Returns:
            str: the padding for the country name
        """
        country_name_rows = country_name_art.split("\n")
        country_name_length = len(country_name_rows[1])
        country_name_padding = ""
        for _ in range(country_name_length):
            country_name_padding += " "
        return country_name_padding

    @staticmethod
    def _pad_country_name(country_name: str) -> str:
        """Pads the country name with the given padding

        Args:
            country_name (str): the country name to pad

        Returns:
            str: the country name padded with the padding
        """
        padding = TextBanner._generate_country_name_padding(
            country_name_art=country_name
        )
        country_name_rows = country_name.split("\n")
        country_name_rows[0] = padding
        country_name_rows[-1] = padding
        padded_country_name = ""
        for row in country_name_rows:
            padded_country_name += row + "\n"
        return padded_country_name[:-1]

    @classmethod
    def _calculate_flag_height(cls, flag: Flag, columns: int) -> int:
        """Calculates the height of the flag

        Args:
            flag (Flag): the flag object to find the height of
            columns (int): the number of columns to display the flag in

        Returns:
            int: the height of the flag
        """
        flag_text = cls.flag_to_text(flag=flag, columns=columns)
        flag_text_rows = flag_text.split("\n")
        flag_height = len(flag_text_rows)
        return flag_height

    @classmethod
    def _find_flag_column_length(cls, flag: Flag, needed_height: int) -> int:
        """Finds the number of columns to display the flag in

        Args:
            flag (Flag): the flag object to display
            needed_height (int): the needed height of the flag

        Returns:
            int: the number of columns to display the flag in
        """
        columns = 10  # Start at a reasonable number of columns
        while True:
            if cls._calculate_flag_height(flag=flag, columns=columns) >= needed_height:
                break
            columns += 1
        return columns

    @classmethod
    def _find_banner_height(cls, flag: Flag) -> int:
        """Finds the height of the banner

        Args:
            flag (Flag): the flag object to display in the banner

        Returns:
            int: the height of the banner
        """
        country_name = cls._generate_country_name(flag)
        country_name_rows = country_name.split("\n")
        banner_height = len(country_name_rows)
        return banner_height

    @classmethod
    def display_text_banner(cls, flag: Flag):
        """Generates a banner of flags and a country name in the terminal

        Args:
            flag (Flag): flag object to display in the banner
        """

        banner_height = cls._find_banner_height(flag=flag)

        flag_column_length = cls._find_flag_column_length(
            flag=flag, needed_height=banner_height
        )

        flag_text = cls.flag_to_text(flag=flag, columns=flag_column_length)
        country_name = cls._generate_country_name(flag)

        banner = cls._generate_text_banner(
            flag_text=flag_text, country_name_text=country_name
        )

        print(banner)

    @classmethod
    def _generate_text_banner(cls, flag_text: str, country_name_text: str) -> str:
        """Generates a banner of flags and a country name in the terminal

        Args:
            flag_text (str): the text representing the flag
            country_name_text (str): the text representing the country name

        Returns:
            str: the banner of flags and a country name
        """
        flag_text_rows = flag_text.split("\n")
        country_name_rows = country_name_text.split("\n")

        banner = ""
        for i in range(len(flag_text_rows)):
            banner += (
                flag_text_rows[i]
                + " "
                + country_name_rows[i]
                + " "
                + flag_text_rows[i]
                + "\n"
            )

        return banner


def generate_flag(country_code: str) -> Flag:
    """Generates a Flag object from the flags.csv file

    Args:
        country_code (str): The country code of the flag to generate

    Returns:
        Flag: The Flag object corresponding to the country code
    """
    with open(resources.files(data) / "flags.csv", mode="r", encoding="utf-8") as f:
        for country_data in csv.reader(f):
            if country_data[0] == country_code:
                flag = Flag(country_code=country_data[0], country_name=country_data[1])
                return flag
    return None
