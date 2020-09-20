import fitz
import random

from classes.Table_Of_Authorities import get_my_toa
from classes.Table_Of_Contents import get_my_toc
from classes.Brief import get_my_brief
from classes.Uploads import get_my_uploads
from classes.Cover import get_my_cover

from utils.upload.allowed_file import allowed_file
from utils.upload.get_ocr_status import get_ocr_status
from utils.cases.add_page_count_to_cases import add_page_count_to_cases
from utils.upload.get_page_footers import get_page_footers
from utils.upload.get_original_text import get_original_text
from utils.upload.check_for_duplicate_files import check_for_duplicate_files


def upload(request):
    UPLOADS = get_my_uploads()
    BRIEF = get_my_brief()

    if allowed_file(request.form['name']):
        name = request.form['name']
        path = request.form['path']
        BRIEF.reset_brief()

        BRIEF.open_document(name, path)

        doc = BRIEF.data['document']

        bad_pages = get_ocr_status(doc)
        BRIEF.set_bad_pages(bad_pages)
        original_text = get_original_text(doc)
        BRIEF.set_original_text(original_text)
        footers = get_page_footers(original_text)
        BRIEF.set_footers(footers)

        UPLOADS.set_brief_file()
        UPLOADS.update_cases()
        COVER = get_my_cover()
        TABLE_OF_CONTENTS = get_my_toc()
        TABLE_OF_AUTHORITIES = get_my_toa()
        TABLE_OF_CONTENTS.reset_toc()
        TABLE_OF_AUTHORITIES.reset_toa()
        COVER.reset_cover()

        return {
            'uploads': UPLOADS.data,
            'toc': TABLE_OF_CONTENTS.data,
            'brief': BRIEF.data_without_document(),
            'toa': TABLE_OF_AUTHORITIES.data,
            'cover': COVER.data
        }
    else:
        return 'bad request!', 406
