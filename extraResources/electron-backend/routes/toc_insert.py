import random

from classes.Table_Of_Contents import get_my_toc


def toc_insert(IDNumber, direction):
    TABLE_OF_CONTENTS = get_my_toc()

    index = TABLE_OF_CONTENTS.find_index_with_IDNumber(IDNumber)

    entries = TABLE_OF_CONTENTS.data['entries']

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
            TABLE_OF_CONTENTS.set_entries(entries)
            TABLE_OF_CONTENTS.check_entries_for_errors()
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
            TABLE_OF_CONTENTS.set_entries(entries)
            TABLE_OF_CONTENTS.check_entries_for_errors()
            return {
                'entries': entries
            }
    else:
        return 'Something went wrong.', 404
