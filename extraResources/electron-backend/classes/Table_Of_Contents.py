import random
from utils.misc.is_number import is_number
from classes.Brief import get_my_brief


class Table_Of_Contents:
    def __init__(self):
        self.data = self.toc_default_values()

    def reset_toc(self):
        self.data = self.toc_default_values()

    def set_page_number_start(self, page_number):
        if str(page_number) != 'False':
            self.data['pageNumberStartForMe'] = page_number
            self.data['pageNumberStartInPdf'] = page_number + 1

    def set_page_number_end(self, toa_page_number):
        if str(toa_page_number) != 'False':
            self.data['pageNumberEndForMe'] = toa_page_number - 1
            self.data['pageNumberEndInPdf'] = toa_page_number

    # def set_loaded(self):
    #     self.data['loaded'] = True

    def set_difference(self):
        entries = self.data['entries']
        for entry in entries:
            pn_for_me = entry['pageNumberForMe']
            pn_in_pdf = entry['pageNumberInPdf']
            if is_number(pn_for_me) == True and is_number(pn_in_pdf) == True:
                difference = int(pn_for_me) - \
                    int(pn_in_pdf)
                self.data['differenceInPageNumbers'] = difference
                break

    def set_original_text(self, original_text):
        self.data['originalText'] = original_text

    def set_entries(self, new_entries):
        self.data['entries'] = new_entries
        self.check_entries_for_errors()

    def find_index_with_IDNumber(self, IDNumber):
        index = False
        entries = self.data['entries']
        for i in range(len(entries)):
            entry = entries[i]
            if entry['id'] == IDNumber:
                return i

        return index

    def check_entries_for_errors(self):
        BRIEF = get_my_brief()
        page_count = BRIEF.data['document'].pageCount
        entries = self.data['entries']

        if len(entries) == 0:
            self.data['tocEntriesError'] = True
            self.data['tocNumbersError'] = True
        else:
            self.data['tocEntriesError'] = False
            self.data['tocNumbersError'] = False

        for i in range(len(entries)):
            text = entries[i]['entry'].strip()
            pn_for_me = entries[i]['pageNumberForMe']
            pn_in_pdf = entries[i]['pageNumberInPdf']

            if len(text) == 0:
                entries[i]['entryTextError'] = True
                self.data['tocEntriesError'] = True
            else:
                entries[i]['entryTextError'] = False

            if is_number(pn_for_me) == False:
                entries[i]['entryNumberError'] = True
                self.data['tocNumbersError'] = True
            else:
                if pn_for_me < 0 or pn_for_me > page_count:
                    entries[i]['entryNumberError'] = True
                    self.data['tocNumbersError'] = True
                else:
                    entries[i]['entryNumberError'] = False

            if is_number(pn_in_pdf) == False or str(pn_in_pdf) == '0' or str(pn_in_pdf) == 'False':
                footer_status = is_pn_in_footers(pn_in_pdf)
                if str(footer_status) == 'False':
                    entries[i]['entryNumberError'] = True
                    self.data['tocNumbersError'] = True
                else:
                    entries[i]['entryNumberError'] = False
            else:
                entries[i]['entryNumberError'] = False
        self.data['entries'] = entries

    def toc_default_values(self):
        return {
            'pageNumberStartForMe': False,
            'pageNumberEndForMe': False,
            'pageNumberStartInPdf': False,
            'pageNumberEndInPdf': False,
            'loaded': False,
            'tocEntriesError': False,
            'tocNumbersError': False,
            'entries': [],
            'originalText': [],
            'differenceInPageNumbers': 0,
            'loaded': False
        }

    def set_loaded(self, boolean):
        self.data['loaded'] = boolean

    def set_entries_to_one(self):
        entries = self.data['entries']
        if len(entries) == 0:
            new_entry = {
                'entry': '',
                'pageNumberForMe': False,
                'pageNumberInPdf': False,
                'id': 'NEW ENTRY' + str(random.random()),
                'error': True
            }
            self.data['entries'].append(new_entry)
            self.data['tocEntriesError'] = True
            self.data['tocNumbersError'] = True


TABLE_OF_CONTENTS = Table_Of_Contents()


def is_pn_in_footers(page_number):
    page_number = str(page_number).strip()
    BRIEF = get_my_brief()
    footers = BRIEF.data['footers']
    is_footer = False
    for i in range(len(footers)):
        if footers[i]['footer'] == page_number:
            return i
    return is_footer


def get_my_toc():
    global TABLE_OF_CONTENTS
    return TABLE_OF_CONTENTS
