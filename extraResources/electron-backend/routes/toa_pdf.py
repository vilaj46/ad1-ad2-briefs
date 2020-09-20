import os
import fitz
from pdfrw import PdfReader, PdfWriter
from pagelabels import PageLabels, PageLabelScheme
from classes.Uploads import get_my_uploads
from classes.Brief import get_my_brief


def toa_pdf():
    UPLOADS = get_my_uploads()
    cases = UPLOADS.data['caseFiles']
    if len(cases) > 0:
        BRIEF = get_my_brief()
        output_path = get_combined_cases_path()
        current_file_name = cases[0]['fileName']
        doc = fitz.open(cases[0]['filePath'])

        for i in range(1, len(cases)):
            current_case = cases[i]
            if current_case['fileName'] != current_file_name:
                current_file_name = current_case['fileName']
                current_open_case = fitz.open(current_case['filePath'])
                doc.insertPDF(current_open_case)
                current_open_case.close()

        starting_page_number = BRIEF.data['pageCountBeforeCases'] + 1
        for i in range(doc.pageCount):
            page = doc.loadPage(i)
            page.insertText((300, 25), str(starting_page_number), 14)
            starting_page_number += 1

        doc.save(output_path, garbage=4, deflate=1)
        doc.close()

        reader = PdfReader(output_path)
        labels = PageLabels.from_pdf(reader)

        start_page_number = cases[0]['pageNumberForMe']
        label = PageLabelScheme(
            startpage=0, firstpagenum=start_page_number)
        labels.append(label)
        labels.write(reader)

        writer = PdfWriter()
        writer.trailer = reader
        writer.write(output_path)
        return output_path


def get_combined_cases_path():
    BRIEF = get_my_brief()
    file_path = BRIEF.data['filePath']
    last_slash = file_path.rindex('\\')
    output_path = file_path[0:last_slash + 1] + 'combined_cases.pdf'
    return output_path
