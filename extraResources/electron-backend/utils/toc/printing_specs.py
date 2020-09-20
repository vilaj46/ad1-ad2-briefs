import fitz
import re


def get_print_specs_page_number(doc):
    for i in reversed(range(doc.pageCount)):
        text = doc.getPageText(i)
        if 'PRINTING SPECIFICATION' in text or 'Printing Specification' in text:
            return i
        else:
            tempText = text.lower()
            tempText = re.sub(' ', '', tempText)
            tempText = re.sub('\n', '', tempText)
            if 'printingspecification' in text:
                return i
    return False


def check_for_printing_specs(entries):
    for entry in entries:
        entry_lowered = entry.lower()
        if 'printing specification statement' in entry_lowered or 'printing specification' in entry_lowered or 'printing spec' in entry_lowered:
            return False
    return True
