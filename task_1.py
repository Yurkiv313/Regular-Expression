import re


def find_emails(text):
    pattern = re.findall(r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})", text)
    return [f"{match[0]}@{match[1]}" for match in pattern]
