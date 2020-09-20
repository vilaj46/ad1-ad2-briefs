def get_conclusion_page_number(doc):
    for i in reversed(range(doc.pageCount)):
        page = doc.loadPage(i)
        text = page.getText()
        text_lowered = text.lower()
        if 'conclusion' in text_lowered:
            return i

    else:
        # Page before the last page which is usually the Printing Specifications Statement
        # This would be difference if the brief was an appellants brief.
        return doc.pageCount - 1
