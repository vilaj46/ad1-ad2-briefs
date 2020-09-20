from classes.Cover import get_my_cover
from classes.Brief import get_my_brief

from utils.misc.format_text import format_text
from utils.misc.split import split
from utils.misc.is_number import is_number


def get_index_number():
    COVER = get_my_cover()
    BRIEF = get_my_brief()

    original_text = BRIEF.data['originalText']
    cover_text = original_text[COVER.data['pageNumberStartForMe']]

    temp_text = format_text(cover_text)

    if 'indexno.' in temp_text:
        index_number_index = temp_text.find('indexno.')
        start_of_index_number = find_start_of_index_number(
            temp_text, index_number_index)
        end_of_index_number = find_end_of_index_number(
            temp_text, index_number_index)

        COVER.set_index_number(
            'formatted', end_of_index_number + '_' + start_of_index_number + '_')

        COVER.set_index_number(
            'unformatted', start_of_index_number + '/' + end_of_index_number,)

        COVER.set_index_number('number', start_of_index_number)
        COVER.set_index_number('year', end_of_index_number)

        index_number_errors = check_for_index_number_error()

        COVER.set_index_number('indexError', index_number_errors['indexError'])
        COVER.set_index_number('yearError', index_number_errors['yearError'])
    else:
        return {
            'formatted': '',
            'unformatted': '',
            'number': '',
            'year': '',
            'yearError': True,
            'indexError': True,
        }


def check_for_index_number_error():
    # { number, year, formatted, unformatted, indexError, yearError }
    COVER = get_my_cover()
    index_number = COVER.data['indexNumber']
    number = index_number['number'].strip()
    is_number_a_number = is_number(number)

    if len(number) > 6 or len(number) < 2 or is_number_a_number == False:
        index_number['indexError'] = True
    else:
        index_number['indexError'] = False

    year = index_number['year'].strip()
    is_year_a_number = is_number(year)

    if len(year) > 4 or len(year) < 2 or len(year) == 3 or is_year_a_number == False:
        index_number['yearError'] = True
    else:
        index_number['yearError'] = False

    return {
        'indexError': index_number['indexError'],
        'yearError': index_number['yearError']
    }


def find_end_of_index_number(text, index_number_index):
    # split string from 'indexnumber' to the end. there is no point in traversing the entire string
    split_text = split(text[index_number_index:len(text)])
    index_of_slash = split_text.index('/')
    split_after_slash = split_text[index_of_slash + 1:len(split_text)]
    for i in range(0, len(split_after_slash)):
        if is_number(split_after_slash[i]) == False:
            index_of_last_number = i
            break

    # Figure out if its 4 digits or 2
    end = ''.join(map(str, split_after_slash[0:index_of_last_number]))
    if len(end) == 4:
        return end[2:len(end)]
    else:
        return end


def find_start_of_index_number(text, index_number_index):
    split_text = split(text[index_number_index:len(text)])
    index_of_slash = split_text.index('/')

    split_until_slash = split_text[0:index_of_slash]
    index_of_last_number = False
    split_until_slash.reverse()

    for i in range(0, len(split_until_slash)):
        if is_number(split_until_slash[i]) == False:
            index_of_last_number = i - 1
            break

    split_until_slash.reverse()

    return ''.join(map(str, split_until_slash[len(split_until_slash) - index_of_last_number - 1:len(split_until_slash)]))
