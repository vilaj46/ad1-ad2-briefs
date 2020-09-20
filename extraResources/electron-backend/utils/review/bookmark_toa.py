from classes.Table_Of_Authorities import get_my_toa


def bookmark_toa(bookmarks):
    TABLE_OF_AUTHORITIES = get_my_toa()
    pn_start_for_me = TABLE_OF_AUTHORITIES.data['pageNumberStartForMe']

    try:
        bookmarks.append(
            [1, 'TABLE OF AUTHORITIES', pn_start_for_me + 1])
        return bookmarks
    except:
        return bookmarks
