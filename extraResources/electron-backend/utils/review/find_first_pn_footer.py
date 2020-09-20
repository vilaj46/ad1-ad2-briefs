from utils.misc.is_number import is_number


def find_first_pn_footer(footers):
    for i in range(len(footers)):
        foot = footers[i]
        if is_number(foot['footer']):
            return i
