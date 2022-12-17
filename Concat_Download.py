import csv
import glob
import download
from download import download_pdf
import os

def write_data_to_file(data_list, filename):
    fields = ['KeyWord','Title','Authors','Abstract','Link','Index']
    filename = 'pdfs' + filename + 'table.csv'
    with open(filename,'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(data_list)
def mkdir(path):
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)
    else:
        print("folder already exists")

csv_list=glob.glob('/Users/williamlast/PycharmProjects/WebScarping_Pubmed/table_test/*.csv')
i = 1

for file_name in csv_list:
    cur_path = 'pdfs/' + file_name.split("/")[6].split(".")[0] + '/'
    mkdir(cur_path)
    with open(file_name,'r',encoding="utf-8") as csvfile:
        new_table =[]
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur_dict = row
            cur_dict["Index"] = i
            link = cur_dict["Link"]
            try:
                my_save_path = '/Users/williamlast/PycharmProjects/WebScarping_Pubmed/pdfs/'
                my_save_path = my_save_path + file_name.split("/")[6].split(".")[0] + '/'
                pdf_name = i
                print(my_save_path)
                download_pdf(my_save_path,pdf_name,link)
            except:
                pass
            new_table.append(cur_dict.values())
            i = i + 1
        filename = '/' + file_name.split("/")[6].split(".")[0] + '/'
        print("Writing To file: {}".format(filename))
        write_data_to_file(new_table, filename)
        i = 1

