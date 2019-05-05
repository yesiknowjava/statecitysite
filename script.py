import os, pyexcel
book = pyexcel.get_book(file_name="states.xlsx")
sheets = book.to_dict()
sheetname = []
statelist = []
path = os.getcwd()

for name in sheets.keys():
    sheetname.append(name)
    row_counter = 0
    for item in book[name]:
        if row_counter > 0:
            if item[1] not in statelist and item[1]:
                statelist.append(item[1])
        row_counter += 1
        
for item in set(statelist):
    if not os.path.isdir(path+"/content/"+item.lower()):
        os.mkdir(path+"/content/"+item.lower())

data_filepath_list = {}
for name in sheets.keys():
    for item in book[name]:
        data_filepath_list[name] = path+"/data/"+item[1].lower()+".csv"

for name in sheets.keys():
    fileobj = open(data_filepath_list[name],"w+")
    item_row_counter = 0
    for item in book[name]:
        if item_row_counter > 0:
            item = [str(i).replace(",", "###") for i in item]
            fileobj.writelines(",".join(item)+"\n")
        item_row_counter += 1
    fileobj.close()
    

for name in sheets.keys():
    row_counter = 0
    index_file_written = False
    for item in book[name]:
        if row_counter > 0:
            if not index_file_written:
                filepath = path+"/content/"+item[1].lower()+"/_index.html"
                fileobj = open(filepath,"w+")
                fileobj.writelines("---\n")
                fileobj.writelines('title: "'+item[1].strip()+'"\n')
                fileobj.writelines("date: 2019-05-01T18:37:07+05:30"+"\n")
                fileobj.writelines("draft: false"+"\n")
                fileobj.writelines('type: "statecity"'+"\n")
                fileobj.writelines("---"+"\n")
                fileobj.close()
                index_file_written = True

            filepath = path+"/content/"+item[1]+"/"+"-".join(item[2].lower().strip().replace("/", "-").replace(",", "###").split(" "))+".html"
            fileobj = open(filepath,"w+")
            fileobj.writelines("---"+"\n")
            fileobj.writelines('title: "'+item[2].strip()+'"\n')
            fileobj.writelines("date: 2019-05-01T18:37:07+05:30"+"\n")
            fileobj.writelines("draft: false"+"\n")
            fileobj.writelines('type: "statecity"'+"\n")
            fileobj.writelines("---"+"\n")
            fileobj.close()
        row_counter += 1


    