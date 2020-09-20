from classes.Table_Of_Contents import get_my_toc
from classes.Table_Of_Authorities import get_my_toa
from classes.Cover import get_my_cover

from utils.toa.get_toa_page_number import get_toa_page_number
from utils.toc.get_toc_page_number import get_toc_page_number
from utils.toc.get_toc_entries_and_numbers import get_toc_entries_and_numbers
from utils.toc.get_toc_text import get_toc_text


def toc():
    TABLE_OF_CONTENTS = get_my_toc()
    TABLE_OF_AUTHORITIES = get_my_toa()

    toc_page_number = TABLE_OF_CONTENTS.data['pageNumberStartForMe']
    toa_page_number = TABLE_OF_AUTHORITIES.data['pageNumberStartForMe']

    loaded = TABLE_OF_CONTENTS.data['loaded']

    if loaded == True:
        return {
            'tocPage': TABLE_OF_CONTENTS.data
        }

    # Check to see if we've loaded it in the TOAPage
    if str(toa_page_number) == 'False':
        toa_page_number = get_toa_page_number()
        # Check to see if it doesn't exist in the document.
        if str(toa_page_number) == 'False':
            TABLE_OF_CONTENTS.set_entries_to_one()
            return {'tocPage': TABLE_OF_CONTENTS.data}, 404
        else:
            # We can find the toc pageNumberEnd
            TABLE_OF_CONTENTS.set_page_number_end(toa_page_number)
    else:
        TABLE_OF_CONTENTS.set_page_number_end(toa_page_number)

    # Check to see if we've loaded it in the CoverPage
    if str(toc_page_number) == 'False':
        toc_page_number = get_toc_page_number()
        if str(toc_page_number) == 'False':
            TABLE_OF_CONTENTS.set_entries_to_one()
            return {'tocPage': TABLE_OF_CONTENTS.data}, 404
        else:
            COVER = get_my_cover()
            cover_pn_end = COVER.data['pageNumberEndForMe']
            TABLE_OF_CONTENTS.set_page_number_start(toc_page_number)
            if str(cover_pn_end) == 'False':
                COVER.set_page_number_end(toc_page_number)
    else:
        COVER = get_my_cover()
        cover_pn_end = COVER.data['pageNumberEndForMe']
        if str(cover_pn_end) == 'False':
            COVER.set_page_number_end(toc_page_number)

    get_toc_text()
    get_toc_entries_and_numbers()
    TABLE_OF_CONTENTS.set_entries_to_one()
    TABLE_OF_CONTENTS.set_loaded(True)
    return {
        'tocPage': TABLE_OF_CONTENTS.data
    }
