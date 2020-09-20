import json

from classes.Table_Of_Contents import get_my_toc
from classes.Cover import get_my_cover

from utils.toc.get_toc_page_number import get_toc_page_number
from utils.covers.get_cover_page_number import get_cover_page_number
from utils.covers.get_department import get_department
from utils.covers.get_index_number import get_index_number
from utils.covers.get_type_of_brief import get_type_of_brief


def covers():
    COVER = get_my_cover()
    TABLE_OF_CONTENTS = get_my_toc()

    toc_page_number = TABLE_OF_CONTENTS.data['pageNumberStartForMe']

    loaded = COVER.data['loaded']

    if loaded == True:
        return {
            'coverPage': COVER.data
        }

    COVER.set_loaded()

    if str(toc_page_number) == 'False':
        toc_page_number = get_toc_page_number()
        if str(toc_page_number) == 'False':
            COVER.set_errors(True)
            return {'coverPage': COVER.data}, 404
        else:
            COVER.set_page_number_end(toc_page_number)
    else:
        COVER.set_page_number_end(toc_page_number)

    cover_page_number = get_cover_page_number()

    if str(cover_page_number) == 'False':
        COVER.set_errors(True)
        return {'coverPage': COVER.data}, 404

    get_department()
    get_index_number()
    get_type_of_brief()

    return {
        'coverPage': COVER.data
    }
