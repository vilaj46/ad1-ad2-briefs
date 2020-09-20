def get_original_text(doc):
    original_text = []
    for i in range(doc.pageCount):
        text = doc.getPageText(i)
        text = text.encode('ascii', 'ignore')
        text = str(text, 'utf-8')
        if len(text) > 0:
            original_text.append(text)
        else:
            original_text.append('')
    return original_text
