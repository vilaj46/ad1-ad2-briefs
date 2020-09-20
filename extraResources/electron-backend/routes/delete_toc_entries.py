from classes.Table_Of_Contents import get_my_toc


def delete_toc_entries():
    TABLE_OF_CONTENTS = get_my_toc()
    TABLE_OF_CONTENTS.set_entries([])
    TABLE_OF_CONTENTS.set_entries_to_one()
    return {
        'entries': TABLE_OF_CONTENTS.data['entries'],
        'tocEntriesError': TABLE_OF_CONTENTS.data['tocEntriesError'],
        'tocNumbersError': TABLE_OF_CONTENTS.data['tocNumbersError']
    }
