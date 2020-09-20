import fitz
import os

from classes.Table_Of_Contents import get_my_toc
from classes.Brief import get_my_brief


def toc_pdf():
    BRIEF = get_my_brief()
    doc = BRIEF.data['document']
    TABLE_OF_CONTENTS = get_my_toc()
    page_number_start = TABLE_OF_CONTENTS.data['pageNumberStartForMe']
    page_number_end = TABLE_OF_CONTENTS.data['pageNumberEndForMe']
    if str(page_number_start) != 'False' and str(page_number_end) != 'False':
        toc_doc = fitz.open()
        toc_doc.insertPDF(doc, from_page=page_number_start,
                          to_page=page_number_end)

        file_path = BRIEF.data['filePath']
        last_slash = file_path.rindex('\\')
        output_path = file_path[0:last_slash + 1] + 'tocPDF.pdf'
        toc_doc.save(output_path)
        toc_doc.close()
        return output_path
    return ''
