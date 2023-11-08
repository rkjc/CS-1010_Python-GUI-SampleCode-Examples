import datetime
# pytz has to be downloaded with pip
# https://pypi.org/project/pytz/
import pytz

myTimeZone = pytz.timezone('US/Pacific')
myCurentTime = datetime.datetime.now(tz=myTimeZone)

print("year= " + str(myCurentTime.year))
print("month= " + str(myCurentTime.month))
print("day= " + str(myCurentTime.day))
print("--------------------------------------")
print(myCurentTime.strftime("%I:%M:%S %p"))
print(myCurentTime.strftime("%A %B %Y"))


# https://www.programiz.com/python-programming/datetime/strftime

