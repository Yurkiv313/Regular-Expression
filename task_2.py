import re


def validate_date_format(date):
    pattern = re.compile(r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$")
    return pattern.match(date) is not None
