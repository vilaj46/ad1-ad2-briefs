from classes.Uploads import get_my_uploads
from classes.Brief import get_my_brief
from classes.Table_Of_Authorities import get_my_toa

from utils.cases.get_case_data_from_multiple_files import get_case_data_from_multiple_files
from utils.cases.get_case_data_from_single_file import get_case_data_from_single_file
from utils.cases.clear_first_page import clear_first_page
from utils.cases.contains_only_pdf import contains_only_pdf


def cases(request):
    all_pdf = contains_only_pdf(request.form)
    if all_pdf == True:
        BRIEF = get_my_brief()
        doc = BRIEF.data['document']

        UPLOADS = get_my_uploads()
        cases_data = []

        if doc != False:  # If we upload the cases after a document is uploaded.
            cases_data = get_cases_data_after_brief_uploaded(request, doc)
        else:  # If we upload the cases before a document is uploaded.
            cases_data = get_cases_data_before_brief_uploaded(request, doc)

        cases = cases_data['casesData']

        brief_path = BRIEF.data['filePath']

        for i in range(len(cases)):
            if cases[i]['filePath'] == brief_path:
                cases[i]['duplicate'] = True
                UPLOADS.set_case_files_error(True)
            else:
                cases[i]['duplicate'] = False

        case_files = []
        form_list = list(request.form)
        for i in range(len(form_list)):
            current_case = cases_data['casesData'][i]
            case_files.append(current_case)

        UPLOADS.set_case_data(cases)
        UPLOADS.set_case_files(case_files)
        UPLOADS.set_display_for_files()

        TABLE_OF_AUTHORITIES = get_my_toa()
        TABLE_OF_AUTHORITIES.set_loaded(False)

        return {
            'uploads': UPLOADS.data
        }


def get_cases_data_before_brief_uploaded(request, doc):
    if len(request.form) == 1:  # Its a single document containing all of our case law
        cases_data = get_case_data_from_single_file(request, 0)
        return {
            'casesData': cases_data,
            'type': 'single'
        }
    else:
        cases_data = get_case_data_from_multiple_files(request, 0)
        return {
            'casesData': cases_data,
            'type': 'multiple'
        }


def get_cases_data_after_brief_uploaded(request, doc):
    if len(request.form) == 1:  # Its a single document containing all of our case law
        cases_data = get_case_data_from_single_file(request, doc.pageCount)
        return {
            'casesData': cases_data,
            'type': 'single'
        }
    else:
        cases_data = get_case_data_from_multiple_files(request, doc.pageCount)
        return {
            'casesData': cases_data,
            'type': 'multiple'
        }
