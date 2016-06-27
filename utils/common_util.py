"""
common functions
"""
from colorama import Fore


def make_colorful_font(text, color=Fore.CYAN, reset_color=Fore.RESET):
    """make text colorful

    :param text: target text
    :param color: font color, default color is Fore.CYAN
    :param reset_color
    :return: colored text
    """
    return color + text + reset_color
