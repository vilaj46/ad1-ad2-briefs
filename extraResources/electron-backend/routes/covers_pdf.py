import fitz
import os

from classes.Cover import get_my_cover
from classes.Brief import get_my_brief


def covers_pdf():
    BRIEF = get_my_brief()
    doc = BRIEF.data['document']
    COVER = get_my_cover()
    page_number_start = COVER.data['pageNumberStartForMe']
    page_number_end = COVER.data['pageNumberEndForMe']
    if str(page_number_start) != 'False' and str(page_number_end) != 'False':
        cover_doc = fitz.open()
        cover_doc.insertPDF(doc, from_page=page_number_start,
                            to_page=page_number_end)

        file_path = BRIEF.data['filePath']
        last_slash = file_path.rindex('\\')
        output_path = file_path[0:last_slash + 1] + 'coverPDF.pdf'
        cover_doc.save(output_path)
        cover_doc.close()
        return output_path
    return ''
