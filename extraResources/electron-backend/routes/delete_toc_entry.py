from classes.Table_Of_Contents import get_my_toc


def delete_toc_entry(IDNumber):
    TABLE_OF_CONTENTS = get_my_toc()
    old_entries = TABLE_OF_CONTENTS.data['entries']
    index = TABLE_OF_CONTENTS.find_index_with_IDNumber(IDNumber)

    if str(index) != 'False':
        new_entries = old_entries[0:index] + \
            old_entries[index + 1:len(old_entries)]

        TABLE_OF_CONTENTS.set_entries(new_entries)
        TABLE_OF_CONTENTS.set_entries_to_one()
        TABLE_OF_CONTENTS.check_entries_for_errors()
        return {
            'entries': new_entries,
            'tocEntriesError': TABLE_OF_CONTENTS.data['tocEntriesError'],
            'tocNumbersError': TABLE_OF_CONTENTS.data['tocNumbersError']
        }
    else:
        TABLE_OF_CONTENTS.set_entries_to_one()
        return 'Something went wrong.', 404
