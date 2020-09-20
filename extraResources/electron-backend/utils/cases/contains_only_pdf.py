def contains_only_pdf(files):
    file_paths = []
    for file_path in files:
        file_paths.append(file_path)

    for file_path in file_paths:
        pd = file_path.lower()[-4:-1]
        if pd + 'f' != '.pdf':
            return False

    return True
