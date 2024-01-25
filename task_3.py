import re


def extract_name_and_domain(email):
    pattern = re.compile(r"^([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$")
    match = pattern.match(email)
    if match:
        return match.groups()
    else:
        return None
