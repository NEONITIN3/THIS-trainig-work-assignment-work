import  datetime
for x in range(0, int(input("enter the no: "))):
    print(datetime.datetime.today()+datetime.timedelta(days=x))

'''calendar'''

import calendar
cal= calendar.TextCalendar(calendar.SUNDAY)
print(cal.formatyear(2022,2,1,1,3))

