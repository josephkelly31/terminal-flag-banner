"""Python module to display a banner of flags in the terminal
"""

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


def display_single_flag_banner(flag: Flag, banner_length: int) -> bool:
    """Function to display a banner made up of a single flag to a terminal

    Args:
        flag (Flag): the Flag object to display to the terminal
        banner_length (int): the number of flags that make up the banner

    Returns:
        bool: whether the flag is displayed (whether exists in the package's flag folder)
    """
    if not flag.flag_image_file_exists:
        print(f"Country: {flag.country_name} ({flag.country_code}) has no flag image!")
        return False

    single_flag_banner = generate_banner_img(flags=[flag for _ in range(banner_length)])
    display_img(image=single_flag_banner)
    return True


def generate_banner_img(flags: list[Flag]) -> Image:
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


def display_flag(flag: Flag) -> bool:
    """Function to display a flag to a terminal

    Args:
        flag (Flag): the Flag object to display to the terminal

    Returns:
        bool: whether the flag is displayed (whether exists in the package's flag folder)
    """
    if not flag.flag_image_file_exists:
        print(f"Country: {flag.country_name} ({flag.country_code}) has no flag image!")
        return False

    display_img(flag.flag_image)
    return True


def display_img(image: Image) -> bool:
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
