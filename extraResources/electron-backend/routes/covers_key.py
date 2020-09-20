from classes.Cover import get_my_cover

from utils.covers.get_index_number import check_for_index_number_error


def covers_key(key, request):
    COVER = get_my_cover()
    if key == 'department':
        COVER.set_department(request.form['value'])
    elif key == 'indexNumber':
        split_value = request.form['value'].split(',')
        index_number_key = split_value[0]
        index_number_value = split_value[1]
        if index_number_key == 'number':
            COVER.set_index_number('number', index_number_value)
        else:
            COVER.set_index_number('year', index_number_value)

        COVER.set_index_number(
            'formatted', COVER.data['indexNumber']['year'] + '_' + COVER.data['indexNumber']['number'] + '_')
        COVER.set_index_number(
            'unformatted', COVER.data['indexNumber']['year'] + '_' + COVER.data['indexNumber']['number'] + '_')

        index_number_errors = check_for_index_number_error()

        if index_number_errors['indexError'] == False and index_number_errors['yearError'] == False:
            if len(index_number_value) == 2:
                COVER.set_index_number('formatted', COVER.data['indexNumber']['year'] +
                                       '_' + COVER.data['indexNumber']['number'] + '_')
            else:
                COVER.set_index_number('formatted', COVER.data['indexNumber']['year'][2:4] +
                                       '_' + COVER.data['indexNumber']['number'] + '_')

    elif key == 'type':
        COVER.set_type_of_brief(request.form['value'])
    elif key == 'defendant':
        COVER.set_party_text('defendant', request.form['value'])
        if len(request.form['value']) == 0:
            COVER.set_party_error('defendant', True)
        else:
            COVER.set_party_error('defendant', False)
    elif key == 'plaintiff':
        COVER.set_party_text('plaintiff', request.form['value'])
        if len(request.form['value']) == 0:
            COVER.set_party_error('plaintiff', True)
        else:
            COVER.set_party_error('plaintiff', False)
    return {
        'coverPage': COVER.data
    }
