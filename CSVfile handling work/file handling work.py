import csv
from datetime import date, datetime
f1=open("error.csv","w+") #error file
f2=open("correctinput.csv","w+") #correct data
date1 = "09-12-1994"
date2 = "01-11-2000"
date3 = "22-02-2023"
# date1 = datetime.strptime(date1, "%d-%m-%Y")

row_list = [
    ["Samson", 394, date1],
    ["XYZ", 23, date2],
    ["Neo", 73, date3],
["nitin", 23, date2],
    ["Neo", 3, date3],
["raam", 93, date2],
    ["shaam", 123, date1],
["harry", 20, date2],
    ["harry3", 23, date3],
["76ghy", 23, date1],
    ["Ne67o", 103, date3],
["XY45", 237, date2],
    ["Neo1", 523, date1]

]

with open('persons.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

ifile = open('persons2.csv', "r")
read = csv.reader(ifile)



# Checking file
import os
sizeflg=False
if os.stat("persons2.csv").st_size == 0:
    print("File is empty")
else:
    sizeflg= True
    print("File is not empty")
file = open('persons2.csv', "r")
# import os
# os.path.getsize('persons.csv')  #returns file size

#name validation
ifile = open('persons2.csv', "r")
read = csv.reader(ifile)

for row in read:
    x1 = row.replace(",", "_")
    spl_list = (x1.split('_'))
    name=spl_list
    nameflg = False
    if type(spl_list[0]) == str and spl_list[0].isalpha():
        nameflg=True
        print("Name is in string")
    else:
        print("Name is not in string")

#age validation

    ageflg=False
    if len(spl_list[1])>=1 and len(spl_list[1])<=2 and spl_list[1].isnumeric():
        ageflg=True
        print("Age is valid")
    else:
        print("age is not valid")

# validation of DOB
    dobflg=False
    flg = True
    tdy =  datetime.now()
    my_row = datetime.strptime(spl_list[2],"%d-%m-%Y")
    try:
        flg = bool(datetime.strptime(spl_list[2],"%d-%m-%Y"))
    except ValueError:
        flg = False
    if flg==True and tdy>my_row:
        dobflg=True
        print("DOB is VALID")
    else:
        print("Invalid DOB =",spl_list[2])

#
# #putting the data into separate file
#     ifile  = open('persons.csv', "r")
#     read = csv.reader(ifile)

    if dobflg == 0 or nameflg == 0 or ageflg == 0 :
        f1.write(str(spl_list)) #error
    else:
        f2.write(str(spl_list)) #correct



    #
    # if dobflg == False or nameflg == False or ageflg == False :
    #     with open('error.csv', 'w', newline='') as f:
    #         writer = csv.writer(f)
    #         writer.writerows(row_list)
    # else:
    #     with open('correctinput.csv', 'w', newline='') as f1:
    #         writer = csv.writer(f1)
    #         writer.writerows(row_list)





