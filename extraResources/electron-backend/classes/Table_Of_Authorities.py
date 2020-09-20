import random
from classes.Uploads import get_my_uploads
from classes.Brief import get_my_brief
from utils.misc.is_number import is_number


class Table_Of_Authorities:
    def __init__(self):
        self.data = self.toa_default_values()

    def set_loaded(self, boolean):
        self.data['loaded'] = boolean

    def set_page_number_start(self, page_number):
        if str(page_number) != 'False':
            self.data['pageNumberStartForMe'] = page_number
            self.data['pageNumberStartInPdf'] = page_number + 1

    def set_page_number_end(self, page_number):
        self.data['pageNumberEndForMe'] = page_number
        self.data['pageNumberEndInPdf'] = page_number + \
            1  # have ot figure out romans

    def reset_toa(self):
        self.data = self.toa_default_values()

    def set_entries(self, new_entries):
        self.data['entries'] = new_entries
        self.check_entries_for_errors()

    def check_entries_for_errors(self):
        entries = self.data['entries']
        UPLOADS = get_my_uploads()
        BRIEF = get_my_brief()
        case_files = UPLOADS.data['caseFiles']
        self.data['toaEntriesError'] = False
        self.data['toaNumbersError'] = False

        for i in range(len(entries)):
            entry = entries[i]['entry'].strip()
            pn_for_me = entries[i]['pageNumberForMe']
            pn_in_pdf = entries[i]['pageNumberInPdf']
            if len(entry) == 0:
                entries[i]['entryTextError'] = True
                self.data['toaEntriesError'] = True
            else:
                entries[i]['entryTextError'] = False

            pn_for_me_string = str(pn_for_me)
            pn_for_me_string = pn_for_me_string.strip()
            if len(case_files) > 0:
                if is_number(pn_for_me) == False or str(pn_for_me) == 'False' or len(pn_for_me_string) == 0:
                    entries[i]['entryNumberError'] = True
                    self.data['toaNumbersError'] = True
                else:
                    try:
                        if pn_in_pdf <= BRIEF.data['pageCountBeforeCases']:
                            entries[i]['entryNumberError'] = True
                            self.data['toaNumbersError'] = True
                        else:
                            entries[i]['entryNumberError'] = False
                    except:
                        entries[i]['entryNumberError'] = True
                        self.data['toaNumbersError'] = True
            else:
                self.data['toaNumbersError'] = False

        self.data['entries'] = entries

    def find_index_with_IDNumber(self, IDNumber):
        index = False
        entries = self.data['entries']
        for i in range(len(entries)):
            entry = entries[i]
            if entry['id'] == IDNumber:
                return i

        return index

    def toa_default_values(self):
        return {
            'pageNumberStartForMe': False,
            'pageNumberEndForMe': False,
            'pageNumberStartInPdf': False,
            'pageNumberEndInPdf': False,
            'loaded': False,
            'toaEntriesError': False,
            'toaNumbersError': False,
            'entries': []
        }

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
            self.data['toaEntriesError'] = True
            self.data['toaNumbersError'] = True


TABLE_OF_AUTHORITIES = Table_Of_Authorities()


def get_my_toa():
    global TABLE_OF_AUTHORITIES
    return TABLE_OF_AUTHORITIES
