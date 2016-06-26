from colorama import Fore


def make_colorful_font(text, color=Fore.CYAN):
    """make text colorful

    :param text: target text
    :param color: font color, default color is Fore.CYAN
    :return: colored text
    """
    return color + text + Fore.RESET
