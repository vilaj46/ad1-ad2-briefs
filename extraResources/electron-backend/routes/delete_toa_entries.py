from classes.Table_Of_Authorities import get_my_toa


def delete_toa_entries():
    TABLE_OF_AUTHORITIES = get_my_toa()
    TABLE_OF_AUTHORITIES.set_entries([])
    TABLE_OF_AUTHORITIES.set_entries_to_one()
    return {
        'entries': TABLE_OF_AUTHORITIES.data['entries'],
        'toaEntriesError': TABLE_OF_AUTHORITIES.data['toaEntriesError'],
        'toaNumbersError': TABLE_OF_AUTHORITIES.data['toaNumbersError']
    }
