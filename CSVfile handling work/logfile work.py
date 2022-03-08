import csv
import logging
from datetime import datetime
from venv import logger

# f_handler = logging.FileHandler('error.log')
# f_handler.setLevel(logging.ERROR)
f1=open("error.csv","w+") #error file
f2=open("correctinput.csv","w+") #correct data
with open('persons.csv', 'r', newline='') as file_obj:
    file1 = open('persons.csv', 'r')
    read = csv.reader(file1)
c=0
nameflag = 0
ageflag = 0
for row in read:
    print(row)
    now = datetime.today()
    cmb_date = row[2] + '/' + row[3] + '/' + row[4]
    my_row = now.strptime(cmb_date, "%d/%m/%Y")

    c=c+1
    if row[0].isalpha():
        print("At row no= ->",c,"at colom 0", row[0],"Name is valid")
        nameflag += 1
    else:
        print("At row no= ->", c, "at colom 0", row[0], "Name is in-valid")


    if len(row[1])>=1 and len(row[1])<=2 and  row[1].isnumeric():
        print("At row no= ->",c,"at colom 1",row[1],"valid age")
        ageflag += 1
    else:
        print("At row no= ->",c,"at colom 1",row[1],"invalid age")

    dobflg=False
    flg = True
    tdy =  datetime.now()
    my_row = datetime.strptime(row[2],"%d/%m/%Y")
    try:
        flg = bool(datetime.strptime(row[2],"%d/%m/%Y"))
    except ValueError:
        flg = False
    if flg==True and tdy>my_row:
        dobflg=True
        print("At row no= ->",c,"at colom 2",row[2],"DOB is VALID")
    else:
        print("At row no= ->",c,"at colom 2","Invalid DOB =",row[2])





    if nameflag==0 or  ageflag==0 or dobflg==0:
        with open('error.csv', 'a') as f:
            f.write(row[0] + ',' + row[1] + ',' + cmb_date + '\n')
        


    else:
        with open('correctinput.csv', 'a') as f:
            f.write(row[0] + ',' + row[1] + ',' + cmb_date+ '\n')

    nameflag=0
    ageflag=0
    dobflg=False

