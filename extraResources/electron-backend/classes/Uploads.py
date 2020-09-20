import random
from classes.Brief import get_my_brief
from classes.Cover import get_my_cover
from utils.misc.find_index_of_entry_with_id import find_index_of_entry_with_id


class Uploads():
    def __init__(self):
        self.data = self.uploads_default_values()

    def uploads_default_values(self):
        return {
            'briefFile': {
                'badPages': '',
                'fileName': '',
                'filePath': '',
                'IDNumber': '',
                'duplicate': False,
                'type': 'brief'
            },
            'caseFiles': [],
            'caseData': [],
            'displayForFiles': [],
            'caseFilesError': False,
        }

    def set_case_files(self, case_files):
        self.data['caseFiles'] = case_files

    def set_case_data(self, case_data):
        self.data['caseData'] = case_data

    def set_display_for_files(self):
        brief_file = self.data['briefFile']
        if len(brief_file['filePath']) > 0:
            self.data['displayForFiles'] = [
                brief_file] + self.data['caseFiles']
        else:
            self.data['displayForFiles'] = self.data['caseFiles']

        COVER = get_my_cover()
        department = COVER.data['department']['text']
        for case in self.data['displayForFiles']:
            if (len(case['badPages']) > 0 or case['duplicate'] == True) and (department == '' or department == 'Second'):
                self.data['caseFilesError'] = True
                break

    def reset_brief_file(self):
        self.data['briefFile']['badPages'] = ''
        self.data['briefFile']['fileName'] = ''
        self.data['briefFile']['filePath'] = ''
        self.data['briefFile']['IDNumber'] = ''
        self.data['briefFile']['duplicate'] = False

        if len(self.data['displayForFiles']) > 0:
            if self.data['displayForFiles'][0]['type'] == 'brief':
                self.data['displayForFiles'] = self.data['displayForFiles'][1:len(
                    self.data['displayForFiles'])]
        else:
            self.data['caseFilesError'] == False

    def reset_uploads(self):
        self.data = self.uploads_default_values()

    def set_brief_file(self):
        BRIEF = get_my_brief()
        self.data['briefFile']['badPages'] = BRIEF.data['badPages']
        self.data['briefFile']['fileName'] = BRIEF.data['fileName']
        self.data['briefFile']['filePath'] = BRIEF.data['filePath']
        self.data['briefFile']['IDNumber'] = random.randrange(1000000000000)
        self.check_brief_for_duplicate()
        self.set_display_for_files()

    def check_brief_for_duplicate(self):
        case_files = self.data['caseFiles']
        if len(case_files) > 0:
            for case in case_files:
                if case['filePath'] == self.data['briefFile']['filePath']:
                    self.data['briefFile']['duplicate'] = True
                    return
        self.data['briefFile']['duplicate'] = False

    def set_case_files_error(self, boolean):
        self.data['caseFilesError'] = boolean

    def delete_case(self, id_number):
        index_of_removed = find_index_of_entry_with_id(
            id_number, self.data['caseFiles'])
        page_count_of_removed = self.data['caseData'][index_of_removed]['pageCount']
        del self.data['caseFiles'][index_of_removed]
        del self.data['caseData'][index_of_removed]
        self.set_display_for_files()

        COVER = get_my_cover()
        department = COVER.data['department']['text']

        if len(self.data['caseFiles']) == 0 and department == '' or department == 'Second':
            self.data['caseFilesError'] = True
        else:
            BRIEF = get_my_brief()
            brief_file_path = BRIEF.data['filePath']
            case_files = self.data['caseFiles']
            error = False

            for i in range(len(case_files)):
                current_index = self.data['caseData'][i]['index']
                if current_index > index_of_removed:
                    self.data['caseData'][i]['index'] = current_index - 1
                    current_pn_for_me = self.data['caseData'][i]['pageNumberForMe']
                    self.data['caseData'][i]['pageNumberForMe'] = current_pn_for_me - \
                        page_count_of_removed
                    self.data['caseFiles'][i]['pageNumberForMe'] = current_pn_for_me - \
                        page_count_of_removed

                if case_files[i]['filePath'] == brief_file_path:
                    self.data['caseFiles'][i]['duplicate'] == True
                    self.data['caseData'][i]['duplicate'] == True
                    self.data['caseFilesError'] = True
                    error = True
                if len(case_files[i]['badPages']) > 0:
                    self.data['caseFilesError'] = True
                    error = True

            if error == False:
                self.data['caseFilesError'] = False

    def update_cases(self):
        BRIEF = get_my_brief()
        additional_pages = BRIEF.data['pageCountBeforeCases']
        case_data = self.data['caseData']
        if len(case_data) > 0:
            for i in range(len(case_data)):
                self.data['caseData'][i]['pageNumberForMe'] = self.data['caseData'][i]['pageNumberForMe'] + additional_pages


UPLOADS = Uploads()


def get_my_uploads():
    global UPLOADS
    return UPLOADS
