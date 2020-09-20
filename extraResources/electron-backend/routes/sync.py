from classes.Table_Of_Contents import get_my_toc
from classes.Table_Of_Authorities import get_my_toa
from classes.Cover import get_my_cover
from classes.Brief import get_my_brief
from classes.Uploads import get_my_uploads


def sync():
    UPLOADS = get_my_uploads()
    UPLOADS.reset_uploads()

    COVER = get_my_cover()
    COVER.reset_cover()

    TABLE_OF_CONTENTS = get_my_toc()
    TABLE_OF_AUTHORITIES = get_my_toa()

    TABLE_OF_CONTENTS.reset_toc()
    TABLE_OF_AUTHORITIES.reset_toa()

    BRIEF = get_my_brief()
    BRIEF.reset_brief()

    return {
        'uploads': UPLOADS.data,
        'cover': COVER.data,
        'toc': TABLE_OF_CONTENTS.data,
        'toa': TABLE_OF_AUTHORITIES.data,
        'brief': BRIEF.data
    }
