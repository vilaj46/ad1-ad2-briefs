# import os


# def is_file_open(file_path):
#     if os.path.exists(file_path):
#         try:
#             # can't rename an open file so an error will be thrown
#             os.rename(file_path, file_path)
#             return False
#         except:
#             return True
#     raise NameError
