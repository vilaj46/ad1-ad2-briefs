from classes.Table_Of_Contents import get_my_toc, is_pn_in_footers

from utils.misc.is_number import is_number


def toc_key(request):
    TABLE_OF_CONTENTS = get_my_toc()

    IDNumber = request.form['IDNumber']
    key = request.form['key']
    value = request.form['value']
    value = value.strip()

    entries = TABLE_OF_CONTENTS.data['entries']
    index = TABLE_OF_CONTENTS.find_index_with_IDNumber(IDNumber)

    if str(index) != 'False':
        if key == 'pageNumberInPdf' and is_number(value) == True:
            value = int(value)
            difference = TABLE_OF_CONTENTS.data['differenceInPageNumbers']
            entries[index]['pageNumberInPdf'] = value
            footer_status = is_pn_in_footers(value)
            if str(footer_status) == 'True':
                entries[index]['pageNumberForMe'] = footer_status
            entries[index]['pageNumberForMe'] = value + difference
        else:
            entries[index][key] = value
        TABLE_OF_CONTENTS.set_entries(entries)
        TABLE_OF_CONTENTS.check_entries_for_errors()
        return {
            'entries': TABLE_OF_CONTENTS.data['entries'],
            'tocEntriesError': TABLE_OF_CONTENTS.data['tocEntriesError'],
            'tocNumbersError': TABLE_OF_CONTENTS.data['tocNumbersError']
        }
    else:
        return 'Something went wrong.', 404
