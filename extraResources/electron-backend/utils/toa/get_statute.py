import re


def get_statute(entry, name_of_case):
    entry = make_ny_the_same(entry)
    name_of_case = make_ny_the_same(name_of_case)
    entry = find_cplr(entry)
    name_of_case = find_cplr(name_of_case)
    entry = strip_part_of_part(entry)
    name_of_case = strip_part_of_part(name_of_case)
    entry = remove_section_signs(entry)
    name_of_case = remove_section_signs(name_of_case)
    entry = remove_sub_rule(entry)
    name_of_case = remove_sub_rule(name_of_case)

    entry = split_entry(entry)  # split for checking
    name_of_case = split_entry(name_of_case)
    return {'entry': entry, 'name_of_case': name_of_case}


def split_entry(entry):
    temp_split_entry = entry.split(' ')
    split_entry = []
    for i in temp_split_entry:
        i = i.strip()
        if len(i) > 0:
            split_entry.append(i)
    return split_entry


def make_ny_the_same(entry):
    ny = ['n.y.']
    for i in ny:
        if i in entry:
            entry = re.sub(i, 'ny', entry)
    return entry


def find_cplr(entry):
    cplr = ['civ. prac. law & rules', 'cplr r']
    for i in cplr:
        if i in entry:
            entry = re.sub(i, 'cplr', entry)
    return entry


def strip_part_of_part(entry):
    # Used to remove part 1 of 13 for example from Kathleens files
    string_to_remove = ', part'
    if string_to_remove in entry:
        entry = re.sub(string_to_remove, '', entry)
    entry = re.sub(r'(\d+) of (\d+)', '', entry)
    return entry


def remove_section_signs(entry):
    entry = re.sub('§', '', entry)
    return entry


def remove_sub_rule(entry):
    entry = re.sub(r'\(\w+\)', '', entry)
    return entry
