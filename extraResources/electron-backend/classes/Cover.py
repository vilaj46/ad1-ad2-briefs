class Cover:
    def __init__(self):
        self.data = self.cover_default_values()

    def reset_cover(self):
        self.data = self.cover_default_values()

    def set_page_number_start(self, page_number):
        if str(page_number) != 'False':
            self.data['pageNumberStartForMe'] = page_number
            self.data['pageNumberStartInPdf'] = page_number + 1

    def set_page_number_end(self, toc_page_number):
        if str(toc_page_number) != 'False':
            self.data['pageNumberEndForMe'] = toc_page_number - 1
            self.data['pageNumberEndInPdf'] = toc_page_number

    def set_loaded(self):
        self.data['loaded'] = True

    def set_department(self, dept):
        if dept != '':
            self.data['department']['text'] = dept
            self.data['department']['error'] = False
        else:
            self.data['department']['error'] = True

    def set_index_number(self, key, value):
        self.data['indexNumber'][key] = value

    def set_type_of_brief(self, type_of_brief):
        if type_of_brief != '':
            self.data['type']['text'] = type_of_brief
            self.data['type']['error'] = False
        else:
            self.data['type']['error'] = True

    def set_num_pages(self, num_pages):
        self.data['numCoverPages'] = num_pages

    def set_party_text(self, party, value):
        self.data[party]['text'] = value

    def set_party_error(self, party, value):
        self.data[party]['error'] = value

    def set_errors(self, boolean):
        self.data['defendant']['error'] = boolean
        self.data['plaintiff']['error'] = boolean
        self.data['indexNumber']['yearError'] = boolean
        self.data['indexNumber']['indexError'] = boolean
        self.data['type']['error'] = boolean
        self.data['department']['error'] = boolean

    def cover_default_values(self):
        return {
            'loaded': False,
            'defendant': {
                'text': '',
                'error': True
            },
            'plaintiff': {
                'text': '',
                'error': True
            },
            'indexNumber': {
                'formatted': '',
                'unformatted': '',
                'number': '',
                'year': '',
                'yearError': False,
                'indexError': False,
            },
            'type': {
                'text': '',
                'error': False
            },
            'department': {
                'text': '',
                'error': False
            },
            'numCoverPages': False,
            'pageNumberStartForMe': False,
            'pageNumberStartInPdf': False,
            'pageNumberEndForMe': False,
            'pageNumberEndInPdf': False,
        }


COVER = Cover()


def get_my_cover():
    global COVER
    return COVER
