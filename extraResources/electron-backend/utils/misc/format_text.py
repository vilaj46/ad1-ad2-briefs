import re


def format_text(text):
    formattedText = text.lower()
    formattedText = re.sub(' ', '', formattedText)
    formattedText = re.sub('\n', '', formattedText)
    return formattedText
