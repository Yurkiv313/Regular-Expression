import re


def validate_phone_number(number):
    pattern = re.compile(r"^\(\d{3}\) \d{3}-\d{4}$")
    return pattern.match(number) is not None
