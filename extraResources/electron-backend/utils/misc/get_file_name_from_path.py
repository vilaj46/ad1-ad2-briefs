def get_file_name_from_path(path):
    path = path.lower()
    index_of_last_back_slash = path.rindex('\\')
    pdf = path.index('.pdf')
    return path[index_of_last_back_slash + 1:pdf]
