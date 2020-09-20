from classes.Table_Of_Contents import get_my_toc
from classes.Brief import get_my_brief


def get_toc_page_number():
    BRIEF = get_my_brief()
    original_text = BRIEF.data['originalText']
    page_number = False
    tables = ['TABLE OF CONTENTS', 'Table of Contents', 'TABLES OF CONTENT',
              'Tables of Content', 'tableofcontents', 'tablesofcontents', 'tablesofcontent']

    for i in range(len(original_text)):
        page_text = original_text[i]
        text_lowered = page_text.lower()
        for toc in tables:
            if toc in page_text or toc in text_lowered:
                page_number = i
                break

    if page_number != False:
        TABLE_OF_CONTENTS = get_my_toc()
        TABLE_OF_CONTENTS.set_page_number_start(page_number)

    return page_number
