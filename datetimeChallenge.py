import datetime
import pytz


#show time by time zone
my_date = datetime.datetime.now(pytz.timezone('US/Pacific'))
print(my_date.strftime("%c"))
#function to compare open and closing time compared to current
def Portland_hours(start, end, current):
    return start <= current <= end
start = datetime.time(9, 0, 0)
end = datetime.time(17, 0, 0)
current = datetime.datetime.now().time()
y = Portland_hours(start, end, current)
if y is False:
    print("HQ is closed")
else:
    print("HQ is open")

#show time by time zone
ny_date = datetime.datetime.now(pytz.timezone('US/Eastern'))
print(ny_date.strftime("%c"))
#function to compare open and closing time compared to current
def NY_hours(start, end, current):
    return start <= current <= end
#adjusted start and end time to what would be hours in New York
start = datetime.time(6, 0, 0)
end = datetime.time(14, 0, 0)
current = datetime.datetime.now().time()
y = NY_hours(start, end, current)
if y is False:
    print("New York office is closed")
else:
    print("New York office is open")

#show time by time zone
lon_date = datetime.datetime.now(pytz.timezone('Europe/London'))
print(lon_date.strftime("%c"))
#function to compare open and closing time compared to current
def London_hours(start, end, current):
    return start <= current <= end
#adjusted start and end time to what would be hours in London
start = datetime.time(1, 0, 0)
end = datetime.time(9, 0, 0)
current = datetime.datetime.now().time()
y = London_hours(start, end, current)
if y is False:
    print("London office is closed")
else:
    print("London office is open")


