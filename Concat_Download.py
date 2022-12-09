import csv
import glob
import download
from download import download_pdf

def write_data_to_file(data_list, filename):
    fields = ['KeyWord','Title','Authors','Abstract','Link','Index']
    filename = 'pdfs/' + filename
    with open(filename,'w') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(data_list)

csv_list=glob.glob('/Users/williamlast/PycharmProjects/WebScarping_Pubmed/table_test/*.csv')
new_table = []
i = 1

for file_name in csv_list:
    with open(file_name,'r',encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cur_dict = row
            cur_dict["Index"] = i
            # link = cur_dict["Link"]
            # try:
            #     my_save_path = '/Users/williamlast/PycharmProjects/WebScarping_Pubmed/pdfs/'
            #     pdf_name = i
            #     download_pdf(my_save_path,pdf_name,link)
            # except:
            #     pass
            new_table.append(cur_dict.values())
            i = i + 1
filename = "table" + ".csv"
print("Writing To file: {}".format(filename))
write_data_to_file(new_table, filename)

