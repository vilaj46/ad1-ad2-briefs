from classes.Table_Of_Contents import get_my_toc


def bookmark_cover(bookmarks):
    TABLE_OF_CONTENTS = get_my_toc()
    pn_start_for_me = TABLE_OF_CONTENTS.data['pageNumberStartForMe']

    try:
        for i in range(0, pn_start_for_me):
            if i == 0:
                bookmarks.append([1, 'COVER', 0])
            else:
                bookmarks.append([1, "COVER CONT'D", i + 1])
        return bookmarks
    except:
        return bookmarks
