
import csv
import datetime

f1=open("error.csv","w+") #error file
f2=open("correctinput.csv","w+") #correct data
with open('persons2.csv', 'r', newline='') as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        for i in row:
            now=datetime.date.today()
            cmb_date = row[2] + '/' + row[3] + '/' + row[4]
            my_row = now.strftime(cmb_date)
        print(my_row)


# name validation
ifile = open('persons2.csv', "r")
read = csv.reader(ifile)
nameflg = False
ageflg = False
for row in read:

    if type(row[0]) == str and row[0].isalpha():
        nameflg=True
        print("Name is in string")
    else:
        print("Name is not in string")

# age validation


    if len(row[1])>=1 and len(row[1])<=2 and row[1].isnumeric():
        ageflg=True
        print("Age is valid")
    else:
        print("age is not valid")

# validation of DOB
    dobflg=False
    flg = True
    tdy =  datetime.now()
    my_row = datetime.strptime(row[2],"%d-%m-%Y")
    try:
        flg = bool(datetime.strptime(row[2],"%d-%m-%Y"))
    except ValueError:
        flg = False
    if flg==True and tdy>my_row:
        dobflg=True
        print("DOB is VALID")
    else:
        print("Invalid DOB =",row[2])


#putting the data into separate file
    ifile  = open('persons2.csv', "r")
    read = csv.reader(ifile)

    if dobflg == 0 or nameflg == 0 or ageflg == 0 :
        f1.write(str(row)) #error
    else:
        f2.write(str(row)) #correct
    nameflg=False
    ageflg=False
    dobflg=False
f1.close()
f2.close()
#     if dobflg == 0 or nameflg == 0 or ageflg == 0 :
#         with open('error2.csv', 'w', newline='') as f:
#             writer = csv.writer(f)
#             writer.writerows(row_list)
#     else:
#         with open('correctinput2.csv', 'w', newline='') as f1:
#             writer = csv.writer(f1)
#             writer.writerows(row_list)

