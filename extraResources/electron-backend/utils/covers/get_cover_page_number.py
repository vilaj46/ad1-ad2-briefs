from classes.Brief import get_my_brief
from classes.Cover import get_my_cover


def get_cover_page_number():

    COVER = get_my_cover()
    BRIEF = get_my_brief()
    original_text = BRIEF.data['originalText']

    cover_page_number_start = False

    for i in range(len(original_text)):
        page_text = original_text[i]
        text_lowered = page_text.lower()
        options = ['To be argued by:',
                   'Franklin Court Press, Inc.',
                   'tobeargued',
                   'franklincourtpress']
        for option in options:
            if option in page_text or option in text_lowered:
                cover_page_number_start = i
                break

    if str(cover_page_number_start) != 'False':
        COVER.set_page_number_start(cover_page_number_start)

    cover_page_number_end = COVER.data['pageNumberEndForMe']

    if str(cover_page_number_start) != 'False' and str(cover_page_number_end) != 'False':
        COVER.set_num_pages(cover_page_number_end +
                            1 - cover_page_number_start)

    return cover_page_number_start
