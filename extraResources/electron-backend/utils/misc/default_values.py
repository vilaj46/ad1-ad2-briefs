def default_values():
    return {
        'pages': {
            'uploadPage': {
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
            },
            'coverPage': {
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
                'numCoverPages': {
                    'number': 0,
                    'error': False
                },
                'pageNumberStartForMe': {
                    'number': False,
                    'error': False,
                },
                'pageNumberStartInPdf': {
                    'number': False,
                    'error': False,
                },
                'pageNumberEndForMe': {
                    'number': False,
                    'error': False,
                },
                'pageNumberEndInPdf': {
                    'number': False,
                    'error': False,
                }
            }
        },
        'briefData': {
            'pageCountBeforeCases': 0,
            'pageCountAfterCases': 0,
            'footers': [],
            'originalText': '',
        },
        'name': '',
        'path': '',
        'duplicate': False,
        'page_count_before_cases': 0,
        'page_count_after_cases': 0,
        'ocr': {
                'hasBeenChecked': False,
                'isOcred': False,
                'badPages': []
        },
        'covers': {
            'loaded': False,
            'defendant': '',
            'department': False,
            'formattedIndexNumber': '',
            'numCoverPages': 0,
            'pageNumberForMe': False,
            'pageNumberInPdf': False,
            'plaintiff': '',
            'unformattedIndexNumber': '',
            'type': '',
            'errors': {
                    'containsCover': False,
                    'indexNumber': False,
                    'year': False,
                    'pageNumber': False,
                    'numCoverPages': False,
                    'defendant': False,
                    'plaintiff': False,
                    'type': False,
                    'department': False,
            }
        },
        'toc': {
            'loaded': False,
            'pageNumberStartForMe': False,
            'pageNumberStartInPdf': False,
            'pageNumberEndForMe': False,
            'pageNumberEndInPdf': False,
            'entries': []
        },
        'toa': {
            'loaded': False,
            'pageNumberStartForMe': False,
            'pageNumberStartInPdf': False,
            'pageNumberEndForMe': False,
            'pageNumberEndInPdf': False,
            'cases': [],
            'combinedCasesPath': '',
            'combinedCasesFileName': '',
            'entries': [],
            'footer_for_hyperlink': None,
            'departmentError': False,
            'createdCasesFile': False,
        },
        'toa_case_type': '',
        'review': {
            'loaded': False,
        },
        'footers': []
    }
