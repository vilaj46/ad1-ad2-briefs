
from pdfrw import PdfReader, PdfWriter
from pagelabels import PageLabels, PageLabelScheme

from classes.Cover import get_my_cover
from classes.Table_Of_Contents import get_my_toc
from classes.Table_Of_Authorities import get_my_toa
from classes.Brief import get_my_brief

from utils.misc.get_romans import get_romans
from utils.review.find_first_pn_footer import find_first_pn_footer


def change_page_labels(output_path):
    reader = PdfReader(output_path)
    labels = PageLabels.from_pdf(reader)

    COVERS = get_my_cover()
    covers = COVERS.data

    TABLE_OF_CONTENTS = get_my_toc()
    toc = TABLE_OF_CONTENTS.data

    TABLE_OF_AUTHORITIES = get_my_toa()
    toa = TABLE_OF_AUTHORITIES.data

    cover_labels = create_cover_labels(
        covers['pageNumberStartForMe'], toc['pageNumberStartForMe'])

    for i in cover_labels:
        labels.append(i)

    toc_labels = create_toc_labels(toc, toa)
    labels.append(toc_labels)

    toa_labels = create_toa_labels(toa)

    labels.append(toa_labels)

    page_labels = create_page_labels(toc, toa)
    labels.append(page_labels)

    labels.write(reader)
    writer = PdfWriter()
    # Not sure what this does, documentation is horrendous.
    writer.trailer = reader
    writer.write(output_path)


def create_page_labels(toc, toa):
    romans = get_romans()
    BRIEF = get_my_brief()
    footers = BRIEF.data['footers']
    pn_end_for_me = toa['pageNumberEndForMe']
    first_pn = find_first_pn_footer(footers)

    if pn_end_for_me == first_pn:
        label = PageLabelScheme(startpage=pn_end_for_me,
                                firstpagenum=int(footers[first_pn]['footer']),
                                style='arabic')
    elif footers[first_pn - 1]['footer'] == None or footers[first_pn - 1]['footer'] in romans:
        if int(footers[first_pn]['footer']) - 1 > 1:
            label = PageLabelScheme(startpage=pn_end_for_me + 1,
                                    firstpagenum=int(
                                        footers[first_pn]['footer']) - 1,
                                    style='arabic')
        else:
            label = PageLabelScheme(startpage=pn_end_for_me + 1,
                                    firstpagenum=1,
                                    style='arabic')
    return label


def create_cover_labels(cover_page_number, toc_page_number):
    labels = []
    if cover_page_number == 0:
        label = PageLabelScheme(startpage=0,
                                style='letters uppercase',
                                prefix="COVE",
                                firstpagenum=18)
        labels.append(label)

    if toc_page_number > 1:
        label = PageLabelScheme(startpage=1,
                                style='letters uppercase',
                                prefix="COVER CONT'",
                                firstpagenum=4)
        labels.append(label)
    return labels


def create_toc_labels(toc, toa):
    BRIEF = get_my_brief()
    footers = BRIEF.data['footers']
    romans = get_romans()

    try:
        toc_pn = toc['pageNumberStartForMe']
        footer_for_search = footers[int(toc_pn)]['footer']

        if footer_for_search in romans:
            roman_as_number = romans.index(footer_for_search) + 1

            if roman_as_number >= 1:
                toc_pn = int(toc_pn)
                label = PageLabelScheme(startpage=toc_pn,
                                        style='roman lowercase',
                                        firstpagenum=roman_as_number)
        elif footer_for_search == None:
            label = PageLabelScheme(startpage=toc_pn,
                                    style='letters lowercase',
                                    prefix='to',
                                    firstpagenum=3)
        return label
    except:
        return


def create_toa_labels(toa):
    BRIEF = get_my_brief()
    footers = BRIEF.data['footers']
    romans = get_romans()
    try:
        toa_pn = toa['pageNumberStartForMe']
        footer_for_search = footers[int(toa_pn)]['footer']

        if footer_for_search in romans:
            roman_as_number = romans.index(footer_for_search) + 1

            if roman_as_number >= 1:
                toa_pn = int(toa_pn)
                label = PageLabelScheme(startpage=toa_pn,
                                        style='roman lowercase',
                                        firstpagenum=roman_as_number)
        elif footer_for_search == None:
            label = PageLabelScheme(startpage=toa_pn,
                                    style='letters lowercase',
                                    prefix='to',
                                    firstpagenum=3)
        return label
    except:
        return
