from classes.Cover import get_my_cover
from classes.Brief import get_my_brief

from utils.misc.format_text import format_text


def get_type_of_brief():
    COVER = get_my_cover()
    BRIEF = get_my_brief()

    original_text = BRIEF.data['originalText']

    cover_text = original_text[COVER.data['pageNumberStartForMe']]

    if 'REPLY BRIEF FOR' in cover_text or 'REPLY BRIEF OF' in cover_text:
        COVER.set_type_of_brief('replybrief')
        return

    temp_text = format_text(cover_text)
    index_of_supreme_court = temp_text.index('supremecourtstate')
    temp_text = temp_text[0:index_of_supreme_court]
    split_by_dash = temp_text.split('-')

    if 'resp' in split_by_dash[1] or 'respondent' == split_by_dash[1]:
        COVER.set_type_of_brief('respbrief')
    elif 'app' in split_by_dash[1] or 'appellant' == split_by_dash[1]:
        COVER.set_type_of_brief('appbrief')
    else:
        is_appellant = find_index_of_status('-appellant', temp_text)
        is_respondent = find_index_of_status('-respondent', temp_text)
        if is_appellant == True:
            COVER.set_type_of_brief('appbrief')
        elif is_respondent == True:
            COVER.set_type_of_brief('respbrief')
        else:
            COVER.set_type_of_brief('')


def find_index_of_status(status, text):
    try:
        index = text.index(status)
        if index > 0:
            return True
    except:
        return False
