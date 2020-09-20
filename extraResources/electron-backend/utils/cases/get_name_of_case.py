import string
import re

from utils.cases.name_of_case_utils.westlaw import get_name_of_case_in_westlaw
from utils.cases.name_of_case_utils.single_lexis import get_name_of_case_in_single_lexis_document


def get_name_of_case(open_case={}, name_from_path={}, text=''):
    metadata_keys = []

    try:
        metadata_keys = open_case.metadata.keys()
    except:
        metadata_keys = None

    if len(text) > 0:  # Single document
        if 'LEXIS' in text or 'LexisNexis' in text:
            return get_name_of_case_in_single_lexis_document(text)
        else:
            # Try and find westlaw name
            name_of_case = get_name_of_case_in_westlaw(
                open_case, name_from_path, text)
            if name_of_case != None:
                return name_of_case
            else:
                return None
    elif 'title' in metadata_keys and open_case.metadata['title'] != None:
        return open_case.metadata['title']
    else:
        name_of_case = get_name_of_case_in_westlaw(open_case, name_from_path)
        if name_of_case != None and len(name_of_case) > 0:
            name_of_case = string.capwords(name_of_case)
            return name_of_case
        else:
            return None
