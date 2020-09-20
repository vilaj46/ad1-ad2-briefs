from utils.misc.get_romans import get_romans


def get_toa_footer(doc, page_number_start):
    romans = get_romans()

    page = doc.loadPage(page_number_start)
    text = page.getText()

    split_text = text.split('\n')
    for i in range(len(split_text)):
        split_text[i] = split_text[i].strip()

    for roman in romans:
        if roman in split_text:
            return roman

    return None
