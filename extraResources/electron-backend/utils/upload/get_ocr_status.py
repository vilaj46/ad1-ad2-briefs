def get_ocr_status(doc):
    bad_pages = check_ocr_status(doc)
    return bad_pages


def check_ocr_status(doc):
    bad_pages = []

    for i in range(doc.pageCount):
        text = doc.getPageText(i)
        text = text.encode('ascii', 'ignore')
        text = str(text, 'utf-8')
        if len(text) == 0:
            bad_pages.append(i)

    bad_pages = create_bad_pages(bad_pages)
    bad_pages = format_bad_pages(bad_pages)

    return bad_pages


def format_bad_pages(bad_pages):
    try:
        separate_bad_pages = bad_pages.split(', ')
        snp = []  # Numbers are strings, we convert them to ints.
        final = []
        for num in separate_bad_pages:
            snp.append(int(num))

        if len(snp) == 1:
            return str(snp[0] + 1)

        for i in range(len(snp)):
            current_index = i

            # If we've reached the last number
            if current_index + 1 == len(snp):
                final.append(str(snp[i] + 1))
                break

            for j in range(i + 1, len(snp)):
                subtract = snp[j] - snp[current_index]
                if subtract != 1:

                    if current_index > i:
                        final.append(str(snp[i] + 1) + ' - ' +
                                     str(snp[current_index] + 1) + ', ')
                    else:
                        final.append(str(snp[i] + 1) + ', ')
                    break
                else:
                    current_index = current_index + 1
            if current_index == len(snp) - 1:
                break

        if len(final) == 0:
            return str(snp[0] + 1) + ' - ' + str(snp[len(snp) - 1] + 1)
        elif len(final) > 0:
            # Some are bad pages. ['1', '7 - 8', '8' '62']
            marked_for_removal = []
            for i in range(len(final)):
                if ' - ' in final[i] and i + 1 < len(final):
                    marked_for_removal.append(i + 1)

            final_to_string = ''

            for i in range(len(final)):
                if i not in marked_for_removal:
                    final_to_string += final[i]

            return final_to_string
        else:
            # Couldn't figure it out
            return bad_pages
    except:
        return ''


def create_bad_pages(pages):
    page_numbers_to_string = []
    for num in pages:
        page_numbers_to_string.append(str(num))
    return ', '.join(page_numbers_to_string)
