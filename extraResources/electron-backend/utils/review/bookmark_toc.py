from classes.Table_Of_Contents import get_my_toc


def bookmark_toc(bookmarks):
    TABLE_OF_CONTENTS = get_my_toc()
    pn_start_for_me = TABLE_OF_CONTENTS.data['pageNumberStartForMe']
    try:
        bookmarks.append(
            [1, 'TABLE OF CONTENTS', pn_start_for_me + 1])
        return bookmarks
    except:
        return bookmarks
