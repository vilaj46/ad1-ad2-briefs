def delete_case(index, my_file):
    toa = my_file.get_attribute('toa')

    toa_case_type = my_file.get_attribute('toa_case_type')

    if toa_case_type == 'single':
        toa['cases'] = []
        my_file.set_attribute('toa', toa)
        return

    cases = toa['cases']

    index = int(index)
    removed_case = cases[index]

    try:
        # We need the following case, and the difference
        # To figure out how many pages the removed case was.
        following_case = cases[index + 1]
        difference = following_case['pageNumberForMe'] - \
            removed_case['pageNumberForMe']

        cases = cases[0:index] + \
            cases[index + 1:len(cases)]

        for i in range(index, len(cases)):
            cases[i]['pageNumberForMe'] = cases[i]['pageNumberForMe'] - difference

        toa['cases'] = cases
        toa['createdCasesFile'] = False
        my_file.set_attribute('toa', toa)

    except:
        # The last case in the list
        cases = cases[0:index] + \
            cases[index + 1:len(cases)]

        toa['cases'] = cases
        toa['createdCasesFile'] = False
        my_file.set_attribute('toa', toa)
