import fitz


class Brief():
    def __init__(self):
        self.data = self.brief_default_values()

    def set_page_count_after_cases(self, page_count):
        self.data['pageCountAfterCases'] = self.data['pageCountBeforeCases'] + page_count

    def set_output_path(self, output_path):
        self.data['outputPath'] = output_path

    def data_without_document(self):
        return {
            'pageCountBeforeCases': self.data['pageCountBeforeCases'],
            'pageCountAfterCases': self.data['pageCountAfterCases'],
            'footers': self.data['footers'],
            'originalText': self.data['originalText'],
            'fileName': self.data['fileName'],
            'filePath': self.data['filePath'],
            'badPages': self.data['badPages'],
            'outputPath': self.data['outputPath']
        }

    def brief_default_values(self):
        return {
            'document': False,
            'pageCountBeforeCases': 0,
            'pageCountAfterCases': 0,
            'footers': [],
            'originalText': '',
            'fileName': '',
            'filePath': '',
            'badPages': '',
            'outputPath': '',
        }

    def set_footers(self, footers):
        self.data['footers'] = footers

    def set_original_text(self, original_text):
        self.data['originalText'] = original_text

    def set_bad_pages(self, bad_pages):
        self.data['badPages'] = bad_pages

    def open_document(self, name, path):
        self.data['fileName'] = name
        self.data['filePath'] = path
        self.data['document'] = fitz.open(path)
        self.data['pageCountBeforeCases'] = self.data['document'].pageCount

    def close_document(self):
        if self.data['document'] != False:
            self.data['document'].close()
            self.reset_brief()

    def reset_brief(self):
        self.data = self.brief_default_values()


BRIEF = Brief()


def get_my_brief():
    global BRIEF
    return BRIEF
