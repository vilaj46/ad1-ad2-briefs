import fitz
import re
import os

from routes.toc import toc

from classes.Table_Of_Contents import get_my_toc
from classes.Table_Of_Authorities import get_my_toa
from classes.Uploads import get_my_uploads
from classes.Brief import get_my_brief

from utils.misc.is_number import is_number
from utils.toa.get_toa_page_number import get_toa_page_number
from utils.toa.get_toa_page_numbers import get_toa_page_numbers
from utils.toa.get_toa_entries import get_toa_entries


def toa():
    TABLE_OF_AUTHORITIES = get_my_toa()
    TABLE_OF_CONTENTS = get_my_toc()
    UPLOADS = get_my_uploads()

    loaded = TABLE_OF_AUTHORITIES.data['loaded']

    if loaded == True:
        return {
            'toaPage': TABLE_OF_AUTHORITIES.data
        }

    toa_pn_to_start = TABLE_OF_AUTHORITIES.data['pageNumberStartForMe']

    if str(toa_pn_to_start) == 'False':
        toa_pn_to_start = get_toa_page_number()
        if str(toa_pn_to_start) == 'False':
            return {'toa': TABLE_OF_AUTHORITIES.data}, 404
        else:
            TABLE_OF_CONTENTS.set_page_number_end(toa_pn_to_start)
    else:
        TABLE_OF_CONTENTS.set_page_number_end(toa_pn_to_start)

    if len(TABLE_OF_CONTENTS.data['entries']) > 0:
        first_entry = TABLE_OF_CONTENTS.data['entries'][0]
        if str(first_entry['pageNumberForMe']) != 'False' and is_number(first_entry['pageNumberForMe']):
            TABLE_OF_AUTHORITIES.set_page_number_end(
                first_entry['pageNumberForMe'])
        else:
            return {'toa': TABLE_OF_AUTHORITIES.data}, 404
    else:
        toc()
        TABLE_OF_AUTHORITIES.set_page_number_end(
            TABLE_OF_CONTENTS.data['entries'][0]['pageNumberForMe'])
    entries = get_toa_entries()
    toa_objects = []
    case_data = UPLOADS.data['caseData']

    if len(case_data) > 0:
        page_numbers = get_toa_page_numbers(entries, case_data)
        toa_objects = create_toa_objects_with_page_numbers(
            entries, page_numbers)
    else:
        toa_objects = create_toa_objects_without_page_numbers(entries)

    TABLE_OF_AUTHORITIES.set_entries(toa_objects)
    TABLE_OF_AUTHORITIES.set_loaded(True)

    return {'toaPage': TABLE_OF_AUTHORITIES.data}


def create_toa_objects_without_page_numbers(entries):
    toa_objects = []
    for i in range(len(entries)):
        toa_objects.append({
            'id': entries[i],
            'pageNumberForMe': 0,
            'pageNumberInPdf': 0,
            'entry': entries[i],
            'error': False,
            'originalEntry': entries[i]
        })
    return toa_objects


def create_toa_objects_with_page_numbers(entries, page_numbers):
    toa_objects = []
    for i in range(len(entries)):
        toa_objects.append({
            'id': entries[i],
            'pageNumberForMe': page_numbers[i] - 1,
            'pageNumberInPdf': page_numbers[i],
            'entry': entries[i],
            'error': False,
            'originalEntry': entries[i]
        })
    return toa_objects
