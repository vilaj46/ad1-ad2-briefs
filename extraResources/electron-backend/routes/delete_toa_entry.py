from classes.Table_Of_Authorities import get_my_toa


def delete_toa_entry(IDNumber):
    TABLE_OF_AUTHORITIES = get_my_toa()
    old_entries = TABLE_OF_AUTHORITIES.data['entries']
    index = TABLE_OF_AUTHORITIES.find_index_with_IDNumber(IDNumber)

    if str(index) != 'False':
        new_entries = old_entries[0:index] + \
            old_entries[index + 1:len(old_entries)]

        TABLE_OF_AUTHORITIES.set_entries(new_entries)
        TABLE_OF_AUTHORITIES.set_entries_to_one()
        TABLE_OF_AUTHORITIES.check_entries_for_errors()
        return {
            'entries': new_entries,
            'toaEntriesError': TABLE_OF_AUTHORITIES.data['toaEntriesError'],
            'toaNumbersError': TABLE_OF_AUTHORITIES.data['toaNumbersError']
        }
    else:
        TABLE_OF_AUTHORITIES.set_entries_to_one()
        return 'Something went wrong.', 404
