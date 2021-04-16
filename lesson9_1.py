import datetime
import time
#date = datetime.date(2021, 12, 14)

#print(date.year)
#print(date.month)
#print(date.day)

#print(datetime.date.today())

#d = datetime.datetime(2021, 12, 14, 4, 50, 4)
#print(d.year)
#print(d.hour)
#print(d.second)

#print(datetime.datetime.today().strftime("%d/%m/%y %H:%M:%S"))

#now = datetime.datetime.now()
#then = datetime.datetime(2021, 3, 14)

#delta = now - then 

#print(delta.days)
#print(delta.seconds)

#seconds = delta.total_seconds()
#hours = seconds// 3600 
#minutes = (seconds % 3600) // 60

#print(hours)
#print(minutes)

#print(time.gmtime())

#print(time.ctime(13000))

#for x in range(5):
#	print(x)
#	time.sleep(1)

#print(time.strftime("%d/%m/%Y %H:%M:%S", time.localtime()))
#print(time.localtime())
#print(time.time())
print(time.ctime(time.time()))