import re

from classes.Table_Of_Authorities import get_my_toa
from classes.Brief import get_my_brief


def get_toa_page_number():
    BRIEF = get_my_brief()
    doc = BRIEF.data['document']
    TABLE_OF_AUTHORITIES = get_my_toa()

    page_number = TABLE_OF_AUTHORITIES.data['pageNumberStartForMe']
    count = 0

    if str(page_number) == 'False':
        for page in range(doc.pageCount):
            if count == 2:
                break
            text = doc.getPageText(page)
            if 'TABLE OF AUTHORITIES' in text or 'Table of Authorities' in text:
                page_number = page
                count = count + 1
            else:
                temp_text = text.lower()
                temp_text = re.sub(' ', '', temp_text)
                temp_text = re.sub('\n', '', temp_text)
                if 'tableofauthorities' in temp_text or 'tableofcases' in temp_text:
                    page_number = page
                    count = count + 1

        TABLE_OF_AUTHORITIES.set_page_number_start(page_number)
        return page_number
    else:
        return page_number
