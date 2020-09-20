import fitz


def clear_first_page(request_form):
    if len(request_form) == 1:
        # Clear pages from single file
        for case_path in request_form:
            doc = fitz.open(case_path)
            for i in range(doc.pageCount):
                page = doc.loadPage(0)
                text = page.getText()
                if 'User Name' in text and 'Date and Time' in text and 'Job Number' in text:
                    doc.deletePage(i)
                    doc.saveIncr()
            doc.close()
    else:
        # check the first page only
        for case_path in request_form:
            open_case = fitz.open(case_path)
            page = open_case.loadPage(0)
            text = page.getText()
            if 'User Name' in text and 'Date and Time' in text and 'Job Number' in text:
                open_case.deletePage(0)
                open_case.saveIncr()
            open_case.close()
