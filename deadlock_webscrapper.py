from bs4 import BeautifulSoup
import requests
import csv
#
#
#
# REFORMAT SO EACH SEPERATE CLASS IS STORED IN ITS OWN VARIABLE
# CREATE AN EMPTY LIST AND ITERATE THROUGH EACH CLASS AND STORE IT IN THE LIST
# TANSFORM THE LIST INTO A CSV USING THE LIST
#

url = "https://tracklock.gg/players"

# Fetches the HTML from target webpage
page = requests.get(url)
# Parses the HTML to allow naviagate the DOM
soup = BeautifulSoup(page.text, features="html.parser")

# initialise the classes for data extraction
classes = ["font-medium text-white hidden md:table-cell","font-medium text-blue-400 hover:text-blue-300 text-sm md:text-base","font-semibold text-orange-400 hidden md:table-cell",
           "text-xs md:text-sm whitespace-nowrap overflow-hidden text-ellipsis max-w-[60px] md:max-w-none","text-[9px] md:text-xs text-gray-400 whitespace-nowrap"]
# Extracts title data
title = soup.find_all(class_="mr-2 select-none")
items = soup.find_all(class_=classes)

data_row= []
data = []
title_names_list = []
# initailise counter to help for formatting of data
counter = 0


# Loops through titles and prints the text contained in the HTML class
for title_names in title:
    print(title_names.text,end=" ")
    title_names_list.append(title_names.text)
print('\n')
# Loops through items and prints the text stored in the mulitple HTML classes store in the classes variable
for item in items:
    text = item.text.replace("(","").replace(")","")
    data_row.append(text)
    # Some trash formattings to remove spaces to help control randomness of names
    print(text.replace(" ",""),end=" ")
    counter += 1
    # Once the disired data from one row is retrieved, i start on a new line
    if counter == 5:
        data.append(data_row)
        print("\n")
        counter = 0
        data_row = []
print("\n")
title_names_list.append("Games played")


with open("deadlock_data1.csv",mode="w",newline="",encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(title_names_list)
    writer.writerows(data)
    














