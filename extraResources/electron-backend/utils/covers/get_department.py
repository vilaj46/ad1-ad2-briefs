from classes.Cover import get_my_cover
from classes.Brief import get_my_brief


def get_department():
    COVER = get_my_cover()
    BRIEF = get_my_brief()

    original_text = BRIEF.data['originalText']

    page_text = original_text[COVER.data['pageNumberStartForMe']]
    text_lowered = page_text.lower()
    index_of_department = text_lowered.index('department')
    page_text = page_text[0:index_of_department]
    split = page_text.split('\n')

    for i in split:
        i = i.strip()
        i_lowered = i.lower()
        if i_lowered == 'second':
            COVER.set_department('Second')
        elif i_lowered == 'first':
            COVER.set_department('First')
        elif 'second department' in text_lowered:
            COVER.set_department('Second')
        elif 'first department' in text_lowered:
            COVER.set_department('First')
        else:
            COVER.set_department('')
