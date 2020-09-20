import re


def get_5531_page_number(doc):
    for i in reversed(range(doc.pageCount)):
        text = doc.getPageText(i)
        if 'Statement Pursuant' in text or '5531' in text:
            return i
        else:
            tempText = text.lower()
            tempText = re.sub(' ', '', tempText)
            tempText = re.sub('\n', '', tempText)
            if 'statementpursuantto' in text or 'statementpursuanttocplrrule5531' in tempText:
                return i
    return False


def check_for_5531(entries):
    for entry in entries:
        entry_lowered = entry.lower()
        if 'statement pursuant to cplr 5531' in entry_lowered or '5531' in entry_lowered:
            return False
    return True
