import stock
from stock import *

file_name_list = get_files_list()
logger.info(f"file_name_list = {file_name_list}")

path_local = './Result.csv'
path_s3 = 'table/Result.csv' 
upload_files(path_local, path_s3)