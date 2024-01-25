import re


def split_text_into_sentences(text):
    pattern = re.compile(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s")
    return pattern.split(text)
