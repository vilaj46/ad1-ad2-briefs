from classes.Table_Of_Authorities import get_my_toa
from classes.Table_Of_Contents import get_my_toc
from classes.Brief import get_my_brief
from classes.Uploads import get_my_uploads

from utils.misc.get_romans import get_romans


def hyperlink_cases():
    UPLOADS = get_my_uploads()
    BRIEF = get_my_brief()
    doc = BRIEF.data['document']
    TABLE_OF_AUTHORITIES = get_my_toa()
    toa = TABLE_OF_AUTHORITIES.data

    entries = toa['entries']
    page_numbers = []

    if len(UPLOADS.data['caseFiles']) > 0:
        for entry in entries:
            page_numbers.append(entry['pageNumberForMe'])

        for i in range(toa['pageNumberStartForMe'], toa['pageNumberEndForMe']):
            page = doc.loadPage(i)
            for j in range(0, len(entries)):
                found_rectangles = page.searchFor(entries[j]['entry'])
                if len(found_rectangles) > 0:
                    for found_rectangle in found_rectangles:
                        try:
                            link = {
                                "kind": 1,  # fitz.LINK_GOTO
                                "page": page_numbers[j],
                                "from": found_rectangle,
                            }
                            page.insertLink(link)
                        except:
                            continue
                else:
                    found_rectangles2 = page.searchFor(
                        entries[j]['originalEntry'])
                    if len(found_rectangles2) > 0:
                        for found_rectangle in found_rectangles2:
                            try:
                                link = {
                                    "kind": 1,  # fitz.LINK_GOTO
                                    "page": page_numbers[j],
                                    "from": found_rectangle,
                                }
                                page.insertLink(link)
                            except:
                                continue
    return


def hyperlink_romans():
    BRIEF = get_my_brief()
    TABLE_OF_CONTENTS = get_my_toc()
    doc = BRIEF.data['document']
    toc = TABLE_OF_CONTENTS.data
    romans = get_romans()
    toc_first_page = toc['pageNumberStartForMe']
    toc_last_page = toc['pageNumberEndForMe']
    for i in range(toc_first_page, toc_last_page + 1):
        page = doc.loadPage(i)
        for roman in romans:
            found_rectangles = page.searchFor(roman)
            roman_to_page_number = find_roman_page_number(roman)
            if roman_to_page_number != None:
                for found_rectangle in found_rectangles:
                    link = {
                        "kind": 1,  # fitz.LINK_GOTO
                        "page": roman_to_page_number,
                        "from": found_rectangle,
                    }

                    page.insertLink(link)

                found_rectangles = page.searchFor(' ' + roman)
                for found_rectangle in found_rectangles:
                    link = {
                        "kind": 1,  # fitz.LINK_GOTO
                        "page": roman_to_page_number,
                        "from": found_rectangle,
                    }
                    page.insertLink(link)


def find_roman_page_number(roman):
    BRIEF = get_my_brief()
    footers = BRIEF.data['footers']
    for footer in footers:
        if roman == footer['footer']:
            return footer['pageNumberForMe']
    return None


def hyperlink_numbers():
    BRIEF = get_my_brief()
    TABLE_OF_CONTENTS = get_my_toc()
    TABLE_OF_AUTHORITIES = get_my_toa()
    doc = BRIEF.data['document']
    toc = TABLE_OF_CONTENTS.data
    toa = TABLE_OF_AUTHORITIES.data

    toc_first_page = toc['pageNumberStartForMe']
    toa_last_page = toa['pageNumberEndForMe']

    page_count_before_cases = BRIEF.data['pageCountBeforeCases']

    last_page_before_numbers = find_last_page_before_numbers(toc, toa)

    page_numbers_to_string = convert_page_numbers_to_string(
        page_count_before_cases)
    page_numbers_to_string.reverse()
    for i in range(toc_first_page, toa_last_page):
        page = doc.loadPage(i)
        previous_rectangles = []
        for num in page_numbers_to_string:
            # The default search for the numbers
            found_rectangles = page.searchFor(num)
            # Sometimes just the number is not found and linked so we add the extra space which helps.
            found_rectangles2 = page.searchFor(' ' + num)
            for found_rectangle in found_rectangles:
                # Check if the rectangles are in the previousRectangles and conntain either the same x0, y0, y1, or x1, y1, y0
                is_previous_rectangle = check_if_previous_rectangle(
                    found_rectangle, previous_rectangles)

                if is_previous_rectangle == False:
                    previous_rectangles.append(found_rectangle)
                    try:
                        # THIS MAY BE LESS THAN OR EQUAL TO
                        if int(num) + last_page_before_numbers - 1 < page_count_before_cases:
                            link = {
                                "kind": 1,  # fitz.LINK_GOTO
                                "page": int(num) + last_page_before_numbers - 1,
                                "from": found_rectangle,
                            }
                            page.insertLink(link)
                    except:
                        continue

            for found_rectangle in found_rectangles2:
                is_previous_rectangle = check_if_previous_rectangle(
                    found_rectangle, previous_rectangles)

                if is_previous_rectangle == False:
                    previous_rectangles.append(found_rectangle)
                    try:
                        # THIS MAY BE LESS THAN OR EQUAL TO
                        if int(num) + last_page_before_numbers - 1 < page_count_before_cases:
                            link = {
                                "kind": 1,  # fitz.LINK_GOTO
                                "page": int(num) + last_page_before_numbers - 1,
                                "from": found_rectangle,
                            }
                            page.insertLink(link)
                    except:
                        continue


def check_if_previous_rectangle(rect, previous):
    for prev in previous:
        if (rect.x0 == prev.x0 and rect.y0 == prev.y0 and rect.y1 == prev.y1) or (rect.x1 == prev.x1 and rect.y1 == prev.y1 and rect.y0 == prev.y0):
            return True
    return False


def convert_page_numbers_to_string(max):
    page_numbers = []
    for i in range(1, max + 1):
        page_numbers.append(str(i))
    return page_numbers


def find_last_page_before_numbers(toc, toa):
    romans = get_romans()
    toc_entries = toc['entries']
    for entry in toc_entries:
        if entry['pageNumberInPdf'] in romans:
            return entry['pageNumberForMe'] + 1
    return toa['pageNumberEndForMe']


def set_borders(first_link):
    next_link = first_link.next
    while(next_link):
        first_link.setBorder(None, width=0, style='S')
        next_link.setBorder(None, width=0, style='S')
        # firstLink.setColors(None, [1.0, 0.0, 0.0])
        # nextLink.setColors(None, [1.0, 0.0, 0.0])
        first_link = next_link
        next_link = next_link.next
