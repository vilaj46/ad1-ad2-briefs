import re

from classes.Table_Of_Contents import get_my_toc
from classes.Brief import get_my_brief

from utils.toc.create_entry_objects import create_entry_objects
from utils.toc.printing_specs import get_print_specs_page_number, check_for_printing_specs
from utils.toc._5531 import get_5531_page_number, check_for_5531
from utils.toc.get_conclusion_page_number import get_conclusion_page_number
from utils.misc.get_romans import get_romans
from utils.misc.create_unified_text import create_unified_text
from utils.misc.is_number import is_number


romans = get_romans()


def get_toc_entries_and_numbers():
    BRIEF = get_my_brief()
    doc = BRIEF.data['document']
    TABLE_OF_CONTENTS = get_my_toc()
    unified_text = create_unified_text(TABLE_OF_CONTENTS.data['originalText'])
    split_text = re.split(r'> ', unified_text)
    split_text_lower = []

    for i in split_text:
        split_text_lower.append(i.lower())

    index_of_authorities = find_entries_about_authorities(split_text_lower)
    split_text = split_text[index_of_authorities + 1:len(split_text)]
    split_text = remove_roman_from_first_entry(
        index_of_authorities, split_text)

    toc_entries = get_toc_entries(split_text)
    toc_entries = remove_footers(toc_entries)
    toc_entries = remove_random_numbers(toc_entries)  # Mannapova
    toc_page_numbers = get_toc_page_numbers(split_text)
    entry_objects = create_entry_objects(toc_entries, toc_page_numbers, doc)

    difference = entry_objects[len(entry_objects) - 1]['pageNumberForMe'] - \
        entry_objects[len(entry_objects) - 1]['pageNumberInPdf']

    do_we_add_conclusion = check_for_conclusion(toc_entries)
    if do_we_add_conclusion == True:
        conclusion_page_number = get_conclusion_page_number(doc)
        entry_objects.append({'entry': 'Conclusion', 'pageNumberForMe': conclusion_page_number,
                              'pageNumberInPdf': conclusion_page_number - difference, 'id': 'Conclusion'})

    do_we_add_printing_specs = check_for_printing_specs(toc_entries)
    if do_we_add_printing_specs == True:
        print_specs_page_number = get_print_specs_page_number(doc)
        entry_objects.append({'entry': 'PRINTING SPECIFICATIONS STATEMENT',
                              'pageNumberForMe': print_specs_page_number, 'pageNumberInPdf':  print_specs_page_number - difference, 'id': 'PRINTING SPECIFICATIONS STATEMENT'})

    do_we_add_5531 = check_for_5531(toc_entries)
    if do_we_add_5531 == True:
        fifty_five_page_number = get_5531_page_number(doc)
        if fifty_five_page_number != False:
            entry_objects.append({'entry': 'STATEMENT PURSUANT TO CPLR RULE 5531',
                                  'pageNumberForMe': fifty_five_page_number, 'pageNumberInPdf':  fifty_five_page_number - difference, 'id': '5531'})

    TABLE_OF_CONTENTS.set_entries(entry_objects)
    TABLE_OF_CONTENTS.set_loaded(True)
    TABLE_OF_CONTENTS.set_difference()
    return entry_objects


def check_for_conclusion(entries):
    entries.reverse()
    for entry in entries:
        entry_lowered = entry.lower()
        if 'conclusion' in entry_lowered:
            return False
    return True


def get_toc_page_numbers(uneditted_entries):
    page_numbers = []
    for entry in uneditted_entries:
        try:
            entry = entry.strip()
            first_white_space = entry.index(' ')
            potential_number = entry[0:first_white_space + 1]
            potential_number = potential_number.strip()
            is_this_a_number = is_number(potential_number)
            if is_this_a_number == True:
                page_numbers.append(int(potential_number))
            else:
                if potential_number in romans:
                    page_numbers.append(potential_number)
        except:
            entry = entry.strip()
            is_this_a_number = is_number(entry)
            if is_this_a_number == True:
                page_numbers.append(int(entry))
    return page_numbers


def get_toc_entries(uneditted_entries):
    editted_entries = []
    for entry in uneditted_entries:
        try:
            first_white_space = entry.index(' ')
            new_entry = entry[first_white_space + 1: len(entry)]
            if len(new_entry) > 0:
                editted_entries.append(new_entry.strip())
        except:
            continue
    return editted_entries


def find_entries_about_authorities(split_text_lower):
    index_of_authorities = False
    for j in range(0, len(split_text_lower)):
        if 'authorities' in split_text_lower[j]:
            index_of_authorities = j
    return index_of_authorities


def remove_roman_from_first_entry(index_of_authorities, split_text):
    if index_of_authorities != False or index_of_authorities == 0:
        for roman in romans:
            roman_string = roman + ' '
            if roman_string in split_text[0]:
                index_of_roman_string = split_text[0].index(roman_string)
                split_text[0] = split_text[0][index_of_roman_string +
                                              len(roman_string): len(split_text[0])]
                # Add a space here because we search for white space in the next functions
                split_text[0] = ' ' + split_text[0]
    return split_text


def remove_footers(toc_entries):
    romans.reverse()
    for i in range(len(toc_entries)):
        for roman in romans:
            try:
                index_of_roman = toc_entries[i].index(roman)
                if index_of_roman == 0:
                    toc_entries[i] = toc_entries[i][0 +
                                                    len(roman) + 1: len(toc_entries[i])]
            except:
                continue
    return toc_entries


def remove_random_numbers(toc_entries):
    new_entries = []
    for entry in toc_entries:
        try:
            entry_to_number = is_number(entry)
            if entry_to_number == False:
                new_entries.append(entry)
        except:
            new_entries.append(entry)

    return new_entries
