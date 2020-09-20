import fitz

from classes.Uploads import get_my_uploads


def create_cases_document():
    UPLOADS = get_my_uploads()
    cases = UPLOADS.data['caseFiles']
    if len(cases) > 0:
        current_file_name = cases[0]['fileName']
        doc = fitz.open(cases[0]['filePath'])

        for i in range(1, len(cases)):
            current_case = cases[i]
            if current_case['fileName'] != current_file_name:
                current_file_name = current_case['fileName']
                current_open_case = fitz.open(current_case['filePath'])
                doc.insertPDF(current_open_case)
                current_open_case.close()

        return doc
    else:
        return False
