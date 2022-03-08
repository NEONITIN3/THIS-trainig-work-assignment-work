import csv
import logging
import os
from datetime import datetime
from venv import logger

f1 = open("clean.csv", "w+")
f2 = open("wrong.csv", "w+")
with open('persons.csv', 'r', newline='') as file_obj:
    file1 = open('persons.csv', 'r')
    rdr = (csv.reader(file1))
file_size = os.stat('persons.csv').st_size
# validate size is not zero
if file_size == 0:
    print("The file is empty: " + str(file_size))
else:
    print("The file is not empty: " + str(file_size))
count = 0
flag1 = 0
flag2 = 0
c = 0
for row in rdr:
    c += 1
    print(row)
    now = datetime.today()
    cmb_date = row[2] + '/' + row[3] + '/' + row[4]
    my_row = now.strptime(cmb_date, "%d/%m/%Y")
    if(row[0].isalpha()==True):
        print("name valid")
        flag1 += 1
    else:
        print("not valid name")
        logging.basicConfig(filename="wrong.csv",
                            format=' %(message)s',
                            filemode='w')
        logger.warning(' %s row has a value ERROR at name ', c)
    # valdate age
    if (int(row[1]) > 0 and int(row[1]) <= 99 and row[1].isnumeric()):
        print("valid age")
        flag2 += 1
    else:
        print("age not valid")
        logging.basicConfig(filename="wrong.csv",
                            format='%(message)s',
                            filemode='w')
        logger.warning(' %s row has a value ERROR at age ', c)
    # validate dob
    dobflg = False
    flg = True
    # tdy = datetime.now()
    my_row = datetime.strptime(cmb_date, "%d/%m/%Y")
    try:
        flg = bool(datetime.strptime(cmb_date, "%d/%m/%Y"))
    except ValueError:
        flg = False
    if flg == True and now > my_row:

        dobflg = True
        print("DOB is correct")
    else:
        print("Invalid DOB =", cmb_date)
        logging.basicConfig(filename="wrong.csv",
                            format='%(message)s',
                            filemode='w')
        logger.warning(' %s row has a value ERROR at dob', c)
    # sortting data

    if (flag1 == 0 or flag2 == 0) or dobflg == False:
        with open('wrong.csv', 'a') as f:

            f.write(str(c)+" "+ row[0] + ',' + row[1] + ',' + cmb_date + '\n')
            #logging.warning("error at")
            # logging.basicConfig(filename="wrong.csv",
            #                 format='%(asctime)s %(message)s',
            #                 filemode='w')
            # logger.warning(' %s row has a value ERROR ', c)
    else:
        with open('clean.csv', 'a') as f:
            f.write(row[0] + ',' + row[1] + ',' + cmb_date + '\n')


    flag1 = 0
    flag2 = 0
    dobflg = False

file_obj.close()
f1.close()
f2.close()