import re

from classes.Brief import get_my_brief

from utils.misc.get_romans import get_romans
from utils.misc.is_number import is_number


def get_page_footers(pages):
    footers_data = []
    romans = get_romans()
    BRIEF = get_my_brief()
    page_count_before_cases = BRIEF.data['pageCountBeforeCases']

    for i in range(len(pages)):
        # page is our text
        page = pages[i]
        footer = find_page_footer(page, romans, page_count_before_cases)
        footers_data.append({
            'footer': footer,
            'pageNumberForMe': i
        })
    return footers_data


def find_page_footer(page_text, romans, page_count_before_cases):
    # Footers are either at the top or bototm of the text.
    split_text = page_text.split('\n')
    for i in range(len(split_text)):
        split_text[i] = split_text[i].strip()

    for potential_footer in split_text:
        is_footer_a_number = is_number(potential_footer)
        if is_footer_a_number == True:
            return potential_footer
        elif potential_footer in romans:
            return potential_footer
        else:
            footer = check_for_reagan_footer(potential_footer)
            if footer != None:
                return footer

    return None


def check_for_reagan_footer(potential_footer):
    m = re.search(r"- \d+ -", potential_footer)
    romans = get_romans()
    if m != None:
        found = m.group(0)
        found = re.sub(r'-', '', found)
        found = found.strip()
        if found in romans or is_number(found):
            return found
    return None
