import re
import random
from utils.misc.is_number import is_number
from utils.misc.get_romans import get_romans

# Can probably combine the two utility functions below


def create_entry_objects(toc_entries, toc_page_numbers, doc):
    toc_entry_objects = []
    romans = get_romans()
    starting_page = 0  # Reduce the pages we have to check when going through the doc

    for i in range(len(toc_entries)):
        if toc_page_numbers[i] in romans:
            # Traverse the doc looking for the roman and the entry
            page_number_for_me = find_roman_and_entry(
                starting_page, toc_entries[i], toc_page_numbers[i], doc)
            IDNumber = create_id(toc_entries[i])
            toc_entry_objects.append(
                {'entry': toc_entries[i], 'pageNumberForMe': page_number_for_me, 'pageNumberInPdf': toc_page_numbers[i],
                 'id': IDNumber,
                 'entryTextError': False, 'entryNumberError': False})

            if page_number_for_me != None:
                starting_page = page_number_for_me
        else:
            page_number_for_me = find_entry_page_number(
                starting_page, toc_entries[i], toc_page_numbers[i], doc)
            IDNumber = create_id(toc_entries[i])
            toc_entry_objects.append(
                {'entry': toc_entries[i], 'pageNumberForMe': page_number_for_me,
                    'pageNumberInPdf': toc_page_numbers[i], 'id': IDNumber, 'entryTextError': False, 'entryNumberError': False}
            )
            if page_number_for_me != None:
                starting_page = page_number_for_me
    toc_entry_objects = unifify_entry_object_page_number_for_me(
        toc_entry_objects)
    return toc_entry_objects


def create_id(entry):
    entry = re.sub(r'\/', '-', entry)
    return entry + str(random.randrange(1000))


def unifify_entry_object_page_number_for_me(toc_entry_objects):
    # Sometimes our pageNumberForMe is None because the text on
    # the toc is different from the text on the page
    # Instead of checking right now, we are just going to assign the None values to the difference of the other ones.
    differences = []  # Get all the differences and make sure they are correct
    for obj in toc_entry_objects:
        if obj['pageNumberForMe'] != None:
            try:
                difference = obj['pageNumberForMe'] - obj['pageNumberInPdf']
                differences.append(difference)
            except:
                differences.append(-1)

    # Count the differences to see which one is probably correct
    correct_differences = {}
    for i in range(len(differences)):
        difference_to_string = str(differences[i])
        correct_difference_keys = correct_differences.keys()
        if difference_to_string in correct_difference_keys:
            correct_differences[difference_to_string] += 1
        else:
            correct_differences[difference_to_string] = 1

    most_likely_difference = 0
    for key in correct_differences.keys():
        if correct_differences[key] >= most_likely_difference:
            most_likely_difference = int(key)

    for i in range(len(toc_entry_objects)):
        current_obj = toc_entry_objects[i]
        # Probably dont need this if we are just changing everything to the difference
        in_pdf_is_number = is_number(current_obj['pageNumberInPdf'])
        if in_pdf_is_number:  # Need a fix for this / roman numeral pageNumberInPdf
            if current_obj['pageNumberForMe'] == None or current_obj['pageNumberForMe'] - current_obj['pageNumberInPdf'] != most_likely_difference:
                toc_entry_objects[i]['pageNumberForMe'] = current_obj['pageNumberInPdf'] + \
                    most_likely_difference

    return toc_entry_objects


def find_entry_page_number(starting_page, entry, page_number, doc):
    # We only need to count if we are checking from the first few pages.
    # Our Table of Contents is throwing the below funciton. We are using
    # 3 because our Table of Contents most likely won't be further away than that.
    count = None  # Using none because 0 is falsy
    if starting_page < 3:
        count = 0
    for i in range(starting_page, doc.pageCount):
        page = doc.loadPage(i)
        text = page.getText()
        split_text = text.split('\n')
        split_text = strip_split_text(split_text)
        if count != None and entry in text:
            count += 1
            if count > 1:
                return i

        if entry in text and str(page_number) in split_text:
            return i
        elif str(page_number) in split_text:
            # This is because there was an entry in the table of contents but not on any page.
            # We will just find the page number and leave it at that
            return i
        else:
            # Check for Reagan numbers
            reagan_number = check_for_reagan_numbers(entry, page_number, text)
            if reagan_number != None:
                return i
    return None


def check_for_reagan_numbers(entry, page_number, text):
    # Reagan formats his footers - number -
    # Sometimes the dashes do not come up on the ocr
    # Seomtimes the dashes do not have spaces between the dashes and numbers
    format_one = '- ' + str(page_number) + ' -'  # Correct one
    format_two = '-' + str(page_number) + '-'  # No Spaces
    format_three = '- ' + str(page_number) + '-'  # Space left, no space right
    format_four = '-' + str(page_number) + ' -'  # No space left, space right
    format_five = str(page_number) + '-'  # Left dash missing, no space
    format_six = '-' + str(page_number)  # Right dash missing, no space
    format_seven = str(page_number) + ' -'  # Left dash missing, space
    format_eight = '- ' + str(page_number)  # Right dash missing, space
    formatted_numbers = [format_one, format_two, format_three,
                         format_four, format_five, format_six, format_seven, format_eight]

    # find up to table of contents because of kathleen putting her docket number in the page.
    temp_text = text.lower()
    toc = ['table of content', 'tables of contents', 'table of contents']

    for t in toc:
        try:
            index_of_toc = temp_text.index(t)
            text = text[index_of_toc + len(t):len(text)]
            break
        except:
            continue
    for formatted_number in formatted_numbers:
        if formatted_number in text and entry in text:
            return page_number
    return None


def find_roman_and_entry(starting_page, entry, roman, doc):
    # reduce the chances of getting it randomly in a string.
    formatted_roman = roman + ' '
    # We will split the page by new lines and also check for the roman to increase our chances of correctness
    for i in range(starting_page, doc.pageCount):
        page = doc.loadPage(i)
        text = page.getText()
        split_text = text.split('\n')
        split_text = strip_split_text(split_text)
        if formatted_roman in text and roman in split_text:
            return i
        elif roman in split_text:
            return i
    return False


def strip_split_text(split_text):
    for i in range(len(split_text)):
        split_text[i] = split_text[i].strip()
    return split_text
