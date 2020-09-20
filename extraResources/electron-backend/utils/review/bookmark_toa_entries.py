from classes.Table_Of_Authorities import get_my_toa

from utils.misc.is_number import is_number


def bookmark_toa_entries(bookmarks):
    TABLE_OF_AUTHORITIES = get_my_toa()
    entries = TABLE_OF_AUTHORITIES.data['entries']

    try:
        if len(entries) > 0:
            for entry in entries:
                pn_in_pdf = int(entry['pageNumberInPdf'])
                error = entry['entryNumberError']
                if str(pn_in_pdf) != 'False' and str(pn_in_pdf) != '0' and is_number(pn_in_pdf) == True and error == False:
                    bookmarks.append(
                        [2, entry['entry'], int(pn_in_pdf)])
                else:
                    bookmarks.append([2, entry['entry'], 1])
        return bookmarks
    except:
        return bookmarks
