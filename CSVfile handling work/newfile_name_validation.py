
import re
# for name in glob.glob('sample_[a-zA-Z]*_*.gz'):
#     print('\t', name)
#x = re.findall(r"\bThe", txt)

# file="sample_harry_090965_5_10.csv.gz"
# x = re.findall("^sample_[a-zA-Z]*_\d{6}_\d{1}_[10]", file)
# print(x)
f1=["sample_neo_098765_10_10.csv.gz","sample_harry_090965_5_10.csv.gz","sample_mana_598765_2_10.csv.gz",
    "sample_bob_096765_6_10.csv.gz", "sample_mona_098265_8_10.csv.gz","sample_neo_098765_1_10.csv.gz",
    "sample_neonitin_098765_2_10.csv.gz","sample_pip_098165_9_10.csv.gz","sample_ram_098765_3_10.csv.gz",
    "sample_sham_098765_4_10.csv.gz","sample_Tom_098765_7_10.csv.gz","sample_Tom_098765_90_10.csv.gz","sample_Tom_098765_23_10.csv.gz"]
for file in f1:
    x=re.search("^sample_[a-zA-Z]*_\d{6}_[0-9]_10.*gz",file)
    z=file.replace(".gz"," ")
    print(z)

    x1 = file.replace(".", "_")
    spl_list = (x1.split('_'))
     # print(name)
    sq_id = spl_list[3]
    if(int(sq_id)>0 and int(sq_id)<10):
        print(x1,": -> Valid")
    elif (int(sq_id)==10):
        x2=file.replace(".csv.gz",".last.dat")
        print(x2)
    else:
        print(x1,":-> Not valid")

#Check if the string starts with "The" and ends with "Spain":

# import re
# for name in glob.glob('sample_[a-zA-Z]*_*.gz'):
#     re.search("^sample_[a-zA-Z]*_[0-9]{6}_[1-9]{1}_10.csv.gz$",name)
#     print('\t', name)

#
# from datetime import datetime
# for name in glob.glob('SAMPLE_[a-zA-Z]*_*.csv'):
#      x=name.replace(".", "_")
#      spl_list = (x.split('_'))
#      # print(name)
#      d_id = spl_list[2]
#      b_num = int(spl_list[3])
#      s_num = int(spl_list[4])
# #d_date= datetime.strptime(d_id,'%Y%m%d')
#      print("date_id = ",d_id,"Batch No.= ",b_num,"Seq No.=",s_num)
#      if b_num in range(1,1000):
#          print("valid batch no.")
#          a=1
#      else:
#          print("batch number is invalid")
#      if s_num in range(1,100000):
#          print("valid seq. no")
#          b=1
#      else:
#          print("seq number is invalid")
#      # format1 = "%Y%m%d"
#      res=False
#      try:
#          res = bool(datetime.strptime(d_id,"%Y%m%d"))
#      except ValueError:
#          res = False
#      print("Date format valid? : " + str(res))
# import re.