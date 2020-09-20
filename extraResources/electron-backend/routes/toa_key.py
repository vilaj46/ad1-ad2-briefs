from utils.misc.is_number import is_number
from classes.Table_Of_Authorities import get_my_toa


def toa_key(request):
    TABLE_OF_AUTHORITIES = get_my_toa()

    IDNumber = request.form['IDNumber']
    key = request.form['key']
    value = request.form['value']
    value = value.strip()

    entries = TABLE_OF_AUTHORITIES.data['entries']
    index = TABLE_OF_AUTHORITIES.find_index_with_IDNumber(IDNumber)

    if str(index) != 'False':
        if key == 'pageNumberInPdf' and is_number(value) == True:
            value = int(value)
            entries[index]['pageNumberInPdf'] = value
            entries[index]['pageNumberForMe'] = value + 1

        else:
            entries[index][key] = value

        TABLE_OF_AUTHORITIES.set_entries(entries)
        TABLE_OF_AUTHORITIES.check_entries_for_errors()
        return {
            'entries': TABLE_OF_AUTHORITIES.data['entries'],
            'toaEntriesError': TABLE_OF_AUTHORITIES.data['toaEntriesError'],
            'toaNumbersError': TABLE_OF_AUTHORITIES.data['toaNumbersError']
        }
    else:
        print('Error Will Robinson!')
        return 'Something went wrong.', 404


def check_if_error_on_page_number(page_number, my_file):

    page_count_before_cases = my_file.get_attribute('page_count_before_cases')
    page_count_after_cases = my_file.get_attribute('page_count_after_cases')

    try:
        new_number = int(page_number)
        max_pages = page_count_before_cases  # for the cover
        # We could also add a feature not to make the page number too large
        # I would have to figure out how many pages are in the cases file.

        if new_number <= max_pages or new_number == 0 or new_number > page_count_after_cases:
            return True
        else:
            return False
    except:
        return True


def check_if_error_on_entry(entry):
    if len(entry) == 0 or entry == 'NEW ENTRY':
        return True
    else:
        return False


def get_any_difference(index_to_skip, entries):
    difference = False

    for i in range(len(entries)):
        if i != index_to_skip:
            try:
                page_number_for_me = int(entries[i]['pageNumberForMe'])
                page_number_in_pdf = int(entries[i]['pageNumberInPdf'])
                if is_number(page_number_for_me) == True and is_number(page_number_in_pdf):
                    return page_number_for_me - page_number_in_pdf
            except:
                continue

    return difference
