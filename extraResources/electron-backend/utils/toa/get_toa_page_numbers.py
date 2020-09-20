import re
import fitz
from nltk import edit_distance
from utils.toa.utils.toa_percents import getPercentFromLetters, getPercentFromSplit, getPercentFromComparison


# Figure out how to handle comparisons better. For example, we had Begley but was ocred a Beglev.
# Check first name letter by letter and give credit accordingly.


def get_toa_page_numbers(entries, cases):
    # FIRST WAY TO FIND THE CASE ASSOCIATED WITH THE ENTRY
    page_numbers = []
    currentHighest = 0
    currentPage = False
    for entry in entries:
        currentHighest = 0
        currentPage = False

        for case in cases:
            # We are getting an error if one of the documents isnt ocred
            if len(case['badPages']) == 0:
                percent = getPercentFromComparison(entry, case['nameOfCase'])
                # With the 20, numbers that did not match will not be assigned
                if percent > currentHighest and percent > 20:
                    currentHighest = percent
                    currentPage = case['pageNumberForMe']
        page_numbers.append(currentPage)

    # SECOND WAY TO FIND THE CASE ASSOCIATED WITH THE ENTRY
    # page_numbers = compare_page_numbers_with_distances(
    #     page_numbers, entries, cases)
    return page_numbers


def compare_page_numbers_with_distances(page_numbers, entries, cases):
    new_page_numbers = []
    for i in range(len(entries)):
        current_page_number = page_numbers[i]
        cases_with_distances = get_cases_with_distances(entries[i], cases)
        first_case = cases_with_distances[0]
        if current_page_number != first_case['number']:
            new_page_numbers.append(False)
        else:
            new_page_numbers.append(current_page_number)
    return new_page_numbers


def find_case_with_page_number(page_number, cases):
    selected_case = False
    for case in cases:
        if page_number == case['number']:
            selected_case = case
            break
    return selected_case


def get_cases_with_distances(entry, cases):
    temp_entry = remove_everything_but_letters_numbers(entry)
    for j in range(len(cases)):
        temp_case_name = remove_everything_but_letters_numbers(
            cases[j]['nameOfCase'])
        distance = edit_distance(temp_entry, temp_case_name)
        cases[j]['distance'] = distance
    cases = sort_cases_by_difference(cases)
    return cases

# Move to misc utils


def remove_everything_but_letters_numbers(temp_str):
    regex = r'\W'
    new_str = re.sub(regex, '', temp_str)
    return new_str.lower()


def sort_cases_by_difference(cases):
    # Move to misc utils Folder
    for i in range(len(cases)):
        already_sorted = True

        for j in range(len(cases) - i - 1):
            if cases[j]['distance'] > cases[j + 1]['distance']:
                cases[j], cases[j + 1] = cases[j + 1], cases[j]
                already_sorted = False

        if already_sorted:
            break

    return cases
