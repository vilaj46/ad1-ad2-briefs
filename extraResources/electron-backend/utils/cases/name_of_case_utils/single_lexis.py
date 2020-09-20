from utils.misc.create_unified_text import create_unified_text


def get_name_of_case_in_single_lexis_document(text):
    unified_text = create_unified_text(text)
    if 'As of: ' in unified_text:
        split_text = text.split('\n')
        index_of_name = find_index_of_name(split_text)
        name_of_case = split_text[index_of_name]
        name_of_case = clean_name_of_case(name_of_case)
        return name_of_case.strip()
    else:
        return None


def clean_name_of_case(name_of_case):
    if name_of_case[0] == '.':
        first_white_space = name_of_case.index(' ')
        return name_of_case[first_white_space + 1:len(name_of_case)]
    return name_of_case


def find_index_of_name(split_text):
    find = ['As of: ', 'PM Z ']
    index_of_name = False
    for i in range(0, len(split_text)):
        for j in find:
            if j in split_text[i]:
                index_of_name = i + 1
    return index_of_name
