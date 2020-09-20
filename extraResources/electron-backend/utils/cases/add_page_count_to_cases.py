def add_page_count_to_cases(page_count, cases):
    for case in cases:
        case['pageNumberForMe'] = case['pageNumberForMe'] + page_count
    return cases
