import re
import string

from classes.Table_Of_Authorities import get_my_toa
from classes.Brief import get_my_brief

from utils.misc.get_romans import get_romans
from utils.misc.create_unified_text import create_unified_text
from utils.misc.is_number import is_number


def get_toa_entries():
    BRIEF = get_my_brief()
    TABLE_OF_AUTHORITIES = get_my_toa()
    doc = BRIEF.data['document']

    page_number_start = TABLE_OF_AUTHORITIES.data['pageNumberStartForMe']
    page_number_end = TABLE_OF_AUTHORITIES.data['pageNumberEndForMe']

    if str(page_number_start) == 'False' or str(page_number_end) == 'False':
        return

    entries = []
    romans = get_romans()
    text_list = []

    for i in range(page_number_start, page_number_end):
        text = doc.getPageText(i)
        text_list.append(text)

    unified_text = create_unified_text(text_list)
    split = split_entries(unified_text)
    entries += split

    for i in range(0, len(entries)):
        for roman in romans:
            try:
                index_of_roman = entries[i].index(roman)
                if index_of_roman == 0:
                    entries[i] = entries[i][len(roman):len(entries[i])]
                    entries[i] = entries[i].strip()
            except:
                continue

    entries = remove_final_dash(entries)
    for i in range(len(entries)):
        entries[i] = entries[i].strip()

    # TABLE_OF_AUTHORITIES.set_entries(entries)
    return entries


def remove_final_dash(entries):
    for i in range(len(entries)):
        if entries[i][int(len(entries[i]) - 1)] == '>':
            entries[i] = entries[i][0:int(len(entries[i]) - 2)]
    return entries


def split_entries(entries):
    split = re.split(r'> \d+|Passim|passim', entries)
    new_entries = []
    for entry in split:
        temp_entry = entry.strip()
        if len(temp_entry) > 0:  # Initially used to check whether our below funcitons will work
            temp_entry = clear_key_words(temp_entry)
            if temp_entry[0] == ',' or temp_entry[0] == '-':  # ... , other page numbers
                # find the first letter then split until the end
                temp_entry = clear_page_numbers(temp_entry)

            # We check the length again because of the clearPageNumbers function.
            is_temp_number = is_number(temp_entry)
            if len(temp_entry) > 0 and is_temp_number != True:
                new_entries.append(temp_entry)

    return new_entries


def clear_footer(entry, current_page_number_for_footer):
    romans = get_romans()
    roman_we_are_looking_for = romans[current_page_number_for_footer - 1]

    try:
        index_of_roman = entry.index(roman_we_are_looking_for)
        if index_of_roman == 0:
            # slice len of the roman + 1 for the white space
            len_of_roman_with_whitespace = len(roman_we_are_looking_for) + 1
            return entry[len_of_roman_with_whitespace:len(entry)]
        else:
            return entry
    except:
        return entry


def clear_key_words(entry):
    words = ['Statutes', 'STATUTES', 'Cases']
    for word in words:
        if word in entry:
            entry = entry.replace(word, '')
    return entry.strip()


def clear_page_numbers(entry):
    stop = False
    for char in range(0, len(entry)):
        if entry[char] in string.ascii_letters:
            stop = char
            break
    if stop == False:
        return ''
    return entry[stop:len(entry)]
