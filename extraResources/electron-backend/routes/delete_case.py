from utils.misc.find_index_of_entry_with_id import find_index_of_entry_with_id
from classes.Uploads import get_my_uploads
from classes.Table_Of_Authorities import get_my_toa


# Most of this was done in the Uploads class file. Figure out
# how to clean it up and move some work over here.
def delete_case(id_number):
    UPLOADS = get_my_uploads()
    UPLOADS.delete_case(id_number)
    TABLE_OF_AUTHORITIES = get_my_toa()
    TABLE_OF_AUTHORITIES.check_entries_for_errors()
    TABLE_OF_AUTHORITIES.set_loaded(False)
    return {
        'uploads': UPLOADS.data
    }
