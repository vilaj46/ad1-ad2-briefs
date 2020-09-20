import fitz
import random

from classes.Brief import get_my_brief

from utils.upload.get_ocr_status import get_ocr_status
from utils.misc.get_file_name_from_path import get_file_name_from_path
from utils.cases.get_name_of_case import get_name_of_case


def get_case_data_from_single_file(request, amount_of_brief_pages):
    data = []
    for case_path in request.form:
        open_case = fitz.open(case_path)
        file_name = get_file_name_from_path(case_path) + '.pdf'
        bad_pages = get_ocr_status(open_case)

        for i in range(0, open_case.pageCount):
            text = open_case.getPageText(i)
            name_of_case = get_name_of_case(open_case, case_path, text)
            case_page_number = i
            if name_of_case != None:
                data.append({'nameOfCase': name_of_case,
                             'pageNumberForMe': case_page_number + amount_of_brief_pages + 1,
                             'fileName': file_name,
                             'filePath': case_path,
                             'badPages': bad_pages,
                             'duplicate': False,
                             'type': 'case',
                             'IDNumber': random.randrange(10000000),
                             'index': 1,
                             'pageCount': open_case.pageCount
                             })
            else:
                contains_metadata = does_document_contain_metadata(open_case)
                if contains_metadata == True:

                    title = open_case.metadata['title'] if open_case.metadata['title'] != None else 'Name of case not found'

                    data.append({'nameOfCase': title,
                                 'pageNumberForMe': case_page_number + amount_of_brief_pages + 1,
                                 'fileName': file_name, 'filePath': case_path,
                                 'badPages': bad_pages,
                                 'duplicate': False,
                                 'type': 'case',
                                 'IDNumber': random.randrange(10000000),
                                 'index': 1,
                                 'pageCount': open_case.pageCount
                                 })
                else:
                    # The case does not have a proper name or metadata
                    data.append({
                        'nameOfCase': 'None',
                        'pageNumberForMe': case_page_number + amount_of_brief_pages + 1,
                        'filename': file_name,
                        'filePath': case_path,
                        'badPages': 'badPages',
                        'duplicate': False,
                        'type': 'case',
                        'IDNumber': random.randrange(10000000),
                        'index': 1,
                        'pageCount': open_case.pageCount
                    })
        data = remove_none_cases(data)
        open_case.close()

        BRIEF = get_my_brief()
        BRIEF.set_page_count_after_cases(data[0]['pageCount'])

        return data


def remove_none_cases(data):
    new_data = []
    for d in data:
        if d['nameOfCase'] != None:
            new_data.append(d)
    return new_data


def does_document_contain_metadata(open_case):
    metadata_keys = open_case.metadata.keys()
    if len(metadata_keys) > 0:
        return True
    else:
        return False
