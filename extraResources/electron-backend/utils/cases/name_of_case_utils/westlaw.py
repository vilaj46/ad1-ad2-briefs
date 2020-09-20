import re


def get_name_of_case_in_westlaw(open_case={}, name_from_path={}, text=''):
    page = open_case.loadPage(0)
    text = page.getText()
    text_lowered = text.lower()
    name_from_path_lowered = name_from_path.lower()
    # We are changing the v to a v. for the purpose of westlaw
    name_from_path_lowered_with_v = re.sub(' v ', ' v. ', name_from_path)
    if name_from_path_lowered in text_lowered or name_from_path_lowered_with_v in text_lowered:
        return name_from_path
    else:
        split_text = text.split('\n')
        split_text = clear_blanks(split_text)
        index_with_name = find_index_with_name(name_from_path, split_text)
        if index_with_name != None:
            return split_text[index_with_name]
        else:
            try:
                if '§' in split_text[0]:
                    # Find the next section sign for the title of the page.
                    index_of_second_section_sign = find_index_of_second_section_sign(
                        split_text)
                    return split_text[index_of_second_section_sign]
                return None
            except:
                return None


def find_index_of_second_section_sign(split_text):
    for i in range(1, len(split_text)):
        if '§' in split_text[i]:
            return i
    else:
        return 0


def find_index_with_name(name_from_path, split_text):
    split_name = name_from_path.split(' ')
    first_part_of_name = split_name[0]
    first_part_of_name = first_part_of_name.strip()
    for i in range(len(split_text)):
        split_text_again = split_text[i].split(' ')
        first_part_of_text = split_text_again[0]
        first_part_of_text = first_part_of_text.strip()
        first_part_of_text = first_part_of_text.lower()
        if first_part_of_name == first_part_of_text:
            return i
        else:
            try:
                index_of_slash = name_from_path.rindex('\\')
                first_white_space = name_from_path[index_of_slash:len(
                    name_from_path)].index(' ')
                plaintiff_name = name_from_path[index_of_slash + 1:
                                                index_of_slash + first_white_space].strip()

                if plaintiff_name.lower() in first_part_of_text:
                    return i
            except:
                return None

    return None


def clear_blanks(split_text):
    new_split_text = []
    for split in split_text:
        if len(split) > 0:
            new_split_text.append(split.strip())
    return new_split_text
