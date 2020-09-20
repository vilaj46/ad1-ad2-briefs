def check_for_duplicate_files(file_path, files):
    for current_file in files:
        if current_file['filePath'] == file_path:
            return True
    return False
