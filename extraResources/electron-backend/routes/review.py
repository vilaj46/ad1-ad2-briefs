import re

from routes.covers import covers
from routes.toc import toc
from routes.toa import toa


from utils.review.change_page_labels import change_page_labels
from utils.review.append_cases_to_doc import append_cases_to_doc
from utils.review.bookmark_toa import bookmark_toa
from utils.review.bookmark_toc import bookmark_toc
from utils.review.bookmark_toa_entries import bookmark_toa_entries
from utils.review.bookmark_toc_entries import bookmark_toc_entries
from utils.review.bookmark_cover import bookmark_cover
from utils.review.hyperlink_brief import hyperlink_cases, hyperlink_numbers, hyperlink_romans
from utils.review.create_cases_document import create_cases_document

from classes.Table_Of_Contents import get_my_toc
from classes.Table_Of_Authorities import get_my_toa
from classes.Brief import get_my_brief
from classes.Uploads import get_my_uploads
from classes.Cover import get_my_cover


def createOutputFile():

    BRIEF = get_my_brief()
    doc = BRIEF.data['document']

    cases_doc = create_cases_document()

    if cases_doc != False:
        doc.insertPDF(cases_doc)
        cases_doc.close()

    hyperlink_numbers()
    hyperlink_romans()
    hyperlink_cases()

    bookmarks = doc.getToC(doc)
    # Reset bookmarks because if we created a file then changed the bookmarks,
    # the changes did not take into effect after creating the file again.
    bookmarks = []

    bookmarks = bookmark_cover(bookmarks)
    bookmarks = bookmark_toc(bookmarks)
    bookmarks = bookmark_toa(bookmarks)
    bookmark_toa_entries(bookmarks)
    bookmark_toc_entries(bookmarks)
    doc.setToC(bookmarks)

    file_path = BRIEF.data['filePath']
    COVER = get_my_cover()
    cover_data = COVER.data

    last_slash = file_path.rindex('\\')

    count = 0
    while count != -1 and count <= 5:
        output_path = ''
        if count == 0:
            output_path = file_path[0:last_slash + 1] + cover_data['indexNumber']['formatted'] + cover_data['plaintiff']['text'] + \
                " v " + cover_data['defendant']['text'] + \
                "_" + cover_data['type']['text'] + ".pdf"
        else:
            output_path = file_path[0:last_slash + 1] + cover_data['indexNumber']['formatted'] + cover_data['plaintiff']['text'] + \
                " v " + cover_data['defendant']['text'] + \
                "_" + cover_data['type']['text'] + \
                '(' + str(count) + ')' + ".pdf"

        try:
            doc.save(output_path, garbage=4, deflate=True, clean=True)

            try:
                change_page_labels(output_path)
                BRIEF.set_output_path(output_path)
                count = -1
            except:
                BRIEF.set_output_path(output_path)
                count = -1
        except:
            count += 1

    return output_path

    # Delete created files.
