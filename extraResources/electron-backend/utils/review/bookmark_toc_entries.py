from classes.Table_Of_Contents import get_my_toc

from utils.misc.is_number import is_number


def bookmark_toc_entries(bookmarks):
    TABLE_OF_CONTENTS = get_my_toc()
    entries = TABLE_OF_CONTENTS.data['entries']
    try:
        if len(entries) > 0:
            for entry in entries:
                error = entry['entryNumberError']
                pn_for_me = int(entry['pageNumberForMe'])
                if str(pn_for_me) != 'False' and str(pn_for_me) != '0' and is_number(pn_for_me) == True and error == False:
                    bookmarks.append(
                        [1, entry['entry'],  int(pn_for_me) + 1])
            return bookmarks
        return bookmarks
    except:
        return bookmarks
