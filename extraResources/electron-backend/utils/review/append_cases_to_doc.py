import fitz


def append_cases_to_doc(doc, cases):
    currentCasePath = ''
    newCases = []
    for case in cases:
        if case['path'] != currentCasePath:
            currentCasePath = case['path']
            openCase = fitz.open(currentCasePath)
            page = openCase.loadPage(0)
            doc.insertPDF(openCase)
            openCase.close()
        newCases.append(case)
    return cases
