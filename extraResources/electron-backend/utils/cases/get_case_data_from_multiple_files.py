import fitz
import random

from classes.Brief import get_my_brief

from utils.misc.get_file_name_from_path import get_file_name_from_path
from utils.upload.get_ocr_status import get_ocr_status
from utils.cases.get_name_of_case import get_name_of_case


def get_case_data_from_multiple_files(request, amount_of_brief_pages):
    data = []
    count = 1
    total_page_count_of_cases = 0
    for case_path in request.form:
        open_case = fitz.open(case_path)

        file_name = get_file_name_from_path(case_path) + '.pdf'
        bad_pages = get_ocr_status(open_case)
        name_of_case = get_name_of_case(open_case, file_name)
        total_page_count_of_cases += open_case.pageCount
        data.append({
            'filePath': case_path,
            'fileName': file_name,
            'pageNumberForMe': amount_of_brief_pages + 1,
            'nameOfCase': name_of_case,
            'badPages': bad_pages,
            'duplicate': False,
            'type': 'case',
            'IDNumber': random.randrange(10000000),
            'pageCount': open_case.pageCount,
            'index': count
        })

        count += 1

        amount_of_brief_pages = amount_of_brief_pages + open_case.pageCount
        open_case.close()
    BRIEF = get_my_brief()
    BRIEF.set_page_count_after_cases(total_page_count_of_cases)
    return data
