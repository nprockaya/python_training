import re


def clear_spaces(string):
    return re.sub(r"\s+", "", string)


def clear_hyphens(string):
    return re.sub("[()-]", "", string)


def clear_spaces_and_hyphens(string):
    return clear_hyphens(clear_spaces(string))
