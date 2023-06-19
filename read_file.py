#reading files in python
#open the file
data_file = open("file.txt", "r")

#creat an empty dictionary
menu_item = {}

#loop through data in the file
for line_of_data in data_file:
    #what do we need to do to each line of data
    #split line of data at the ","(string
    #create an entry to the dictionary
    key_values = line_of_data.split(", ")

    #create an enrty to the dictionary. remember to covert price to float
    menu_item[key_values[0]] = float(key_values[1])

#close file
data_file.close()

for item, price in menu_item.items():
    print(f"{item}: ${price:.2f}")