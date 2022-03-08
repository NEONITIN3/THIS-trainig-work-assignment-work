#sample work

# for name in glob.glob('*.csv'):
#     print(name)

#SAMPLE_<table_name>_<date_id>_<batch_no>_<sequence_no>.csv
# where,
# batch_no is in range (001 – 999)
# Date_id will be in format - YYYYMMDD
# sequence no is in range (00001 – 99999)

#1st case
#print WHICH HAVE "SAMPLE_'
# for name in glob.glob('SAMPLE_*.csv'):
#     print('\t', name)

#2 CASE
import glob
for name in glob.glob('SAMPLE_[a-zA-Z]*_*.csv'):
    print('\t', name)

#
from datetime import datetime
for name in glob.glob('SAMPLE_[a-zA-Z]*_*.csv'):
     x=name.replace(".", "_")
     spl_list = (x.split('_'))
     # print(name)
     d_id = spl_list[2]
     b_num = int(spl_list[3])
     s_num = int(spl_list[4])
#d_date= datetime.strptime(d_id,'%Y%m%d')
     print("date_id = ",d_id,"Batch No.= ",b_num,"Seq No.=",s_num)
     if b_num in range(1,1000):
         print("valid batch no.")
         a=1
     else:
         print("batch number is invalid")
     if s_num in range(1,100000):
         print("valid seq. no")
         b=1
     else:
         print("seq number is invalid")
     # format1 = "%Y%m%d"
     res=False
     try:
         res = bool(datetime.strptime(d_id,"%Y%m%d"))
     except ValueError:
         res = False
     print("Date format valid? : " + str(res))
import re.

