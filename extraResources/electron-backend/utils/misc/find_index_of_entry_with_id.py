def find_index_of_entry_with_id(id_number, entries):
    # FOR UPLOADS AND DELETE CASE
    try:
        for i in range(len(entries)):
            if entries[i]['id'] == id_number:
                return i
        return None
    except:
        # FOR FILES
        for i in range(len(entries)):
            if str(entries[i]['IDNumber']) == str(id_number):
                return i
        return None
