import csv

#Get the length of the dictionary by adding items per iteration in a single list
def get_length(file_path):
    with open(file_path) as csvfile:
        reader = csv.reader(csvfile)
        reader_list = list(reader)
        return len(reader_list)

#append data to the file by adding to a existing one
def append_data(file_path, name, email):
    #specify fielf name which can be added in the first iteration by adding the writeheader() function
    fieldnames = ["id", "name", "email"]
    next_id =get_length(file_path) + 1 # +1 is added if there is no writeheader function is applied
    with open(file_path, "a" ,newline = "") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({"id": next_id, "name": name, "email": email})

#example append
#append_data("filelocation", "Aamir", "a@yahoo.com")
