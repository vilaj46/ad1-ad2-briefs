from doc import get_my_doc, set_my_doc

from classes.Table_Of_Contents import get_my_toc
from classes.Table_Of_Authorities import get_my_toa
from classes.Brief import get_my_brief
from classes.Cover import get_my_cover
from classes.Uploads import get_my_uploads


def reset():
    BRIEF = get_my_brief()

    BRIEF.close_document()
    BRIEF.reset_brief()

    UPLOADS = get_my_uploads()
    UPLOADS.reset_brief_file()

    COVER = get_my_cover()
    COVER.reset_cover()

    TABLE_OF_CONTENTS = get_my_toc()
    TABLE_OF_AUTHORITIES = get_my_toa()

    TABLE_OF_CONTENTS.reset_toc()
    TABLE_OF_AUTHORITIES.reset_toa()
    return {
        'uploads': UPLOADS.data,
        'toa': TABLE_OF_AUTHORITIES.data,
        'brief': BRIEF.data,
        'toc': TABLE_OF_CONTENTS.data,
        'cover': COVER.data
    }
