import random

from classes.Table_Of_Authorities import get_my_toa


def toa_insert(IDNumber, direction):
    TABLE_OF_AUTHORITIES = get_my_toa()

    index = TABLE_OF_AUTHORITIES.find_index_with_IDNumber(IDNumber)

    entries = TABLE_OF_AUTHORITIES.data['entries']

    if str(index) != 'False':
        if int(direction) == 1:
            new_entry = {
                'entry': '',
                'pageNumberForMe': False,
                'pageNumberInPdf': False,
                'id': 'NEW ENTRY' + str(random.random()),
                'error': True
            }

            entries.insert(index, new_entry)
            TABLE_OF_AUTHORITIES.set_entries(entries)
            TABLE_OF_AUTHORITIES.check_entries_for_errors()
            return {
                'entries': entries
            }
        else:
            new_entry = {
                'entry': '',
                'pageNumberForMe': False,
                'pageNumberInPdf': False,
                'id': 'NEW ENTRY' + str(random.random()),
                'error': True
            }

            entries.insert(index + 1, new_entry)
            TABLE_OF_AUTHORITIES.set_entries(entries)
            TABLE_OF_AUTHORITIES.check_entries_for_errors()
            return {
                'entries': entries
            }
    else:
        return 'Something went wrong.', 404
