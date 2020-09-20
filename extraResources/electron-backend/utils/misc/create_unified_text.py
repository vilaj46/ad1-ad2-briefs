import re

from utils.misc.find_white_space import find_white_space
from utils.misc.get_romans import get_romans


def create_unified_text(text):
    text_string = ''
    count = 0  # Helps remove footers on the page.

    for t in text:
        temp_text = remove_ellipses(t)
        temp_text = clear_tab_dots(temp_text)
        temp_text = clear_new_lines(temp_text)
        temp_text = clear_gaier_dots(temp_text)
        temp_text = unify_arrows(temp_text)
        temp_text = clear_multiple_spaces(temp_text)
        temp_text = remove_footer(temp_text, count)
        temp_text = remove_toa(temp_text)
        text_string += temp_text
        count += 1
    return text_string


def remove_footer(temp_text, page):
    try:
        romans = get_romans()
        roman = romans[page]
        index_of_roman = temp_text.index(roman)
        if index_of_roman == 0:
            new_temp_text = temp_text[index_of_roman +
                                      len(roman): len(temp_text)]
            return new_temp_text
        return temp_text
    except:
        return temp_text


def remove_ellipses(text):
    ellipses = '…'
    temp_text = text
    if ellipses in text:
        temp_text = re.sub(ellipses, '.', text)
    return temp_text


def remove_toa(text):
    temp_text = text.lower()
    remove = ['table of authorities', 'table of cases',
              'caselaw:', 'caselaw', 'cases', 'page', 'statutes & regulations']
    for i in remove:
        if i in temp_text:
            index_of_removed = temp_text.find(i)
            if index_of_removed <= 30:
                text = text[index_of_removed + len(i) + 1: len(text)]
                temp_text = temp_text[index_of_removed + len(i) + 1: len(text)]
    return text


def unify_arrows(text):
    temp_text = re.sub(' > > ', '>', text)
    temp_text = re.sub('>', ' > ', temp_text)
    return temp_text


def clear_multiple_spaces(text):
    temp_text = re.sub(r'\s{2,}', ' ', text)
    return temp_text


def clear_gaier_dots(text):
    temp_text = text
    if '. .' in text:
        split_text = split(text)
        for index in range(len(split_text)):
            char = split_text[index]
            next_char = try_and_get_char(index, 1, split_text)
            following_char = try_and_get_char(index, 2, split_text)
            if char == '.' and next_char == '.':
                split_text[index] = '>'
            elif char == '.' and next_char == ' ' and following_char == '.':
                split_text[index] = '>'
        for index in range(len(split_text)):
            before_char = try_and_get_char(index, -1, split_text)
            char = split_text[index]
            next_char = try_and_get_char(index, 1, split_text)
            if char == '.' and (before_char == '' or before_char == ' ') and (next_char == '' or next_char == ' '):
                split_text[index] = '>'
        temp_text = ''.join(split_text)
        temp_text = re.sub(r'(>\s){2,}', '>', temp_text)
    return temp_text


def try_and_get_char(index, spaces, text):
    char = False
    try:
        char = text[index + spaces]
        return char
    except:
        return False


def clear_new_lines(text):
    temp_text = re.sub(r'\n', '', text)
    return temp_text


def clear_tab_dots(text):
    temp_text = re.sub(r'\.{2,}', '>', text)
    return temp_text


def split(word):
    return [char for char in word]
