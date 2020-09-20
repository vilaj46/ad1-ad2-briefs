from classes.Table_Of_Contents import get_my_toc
from classes.Brief import get_my_brief


def get_toc_text():
    BRIEF = get_my_brief()
    doc = BRIEF.data['document']
    TABLE_OF_CONTENTS = get_my_toc()

    toc_page_number_start = TABLE_OF_CONTENTS.data['pageNumberStartForMe']
    toc_page_number_end = TABLE_OF_CONTENTS.data['pageNumberEndForMe']

    toc_text = []

    if str(toc_page_number_start) != 'False' and str(toc_page_number_end) != 'False':
        for i in range(toc_page_number_start, toc_page_number_end + 1):
            text = doc.getPageText(i)
            toc_text.append(text)
    else:
        return

    TABLE_OF_CONTENTS.set_original_text(toc_text)
    return toc_text
