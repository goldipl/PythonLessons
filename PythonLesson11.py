print('=== FUNCTIONS === 01 ===')

def PrintHelloPython():
    print('Hello Python!')
    return

PrintHelloPython()

'''
=== FUNCTIONS === 01 ===
Hello Python!
'''

print('=== FUNCTIONS === 02 ===')

from datetime import date
from datetime import timedelta

day = date.today()

if day.weekday() == 5:
    workingday = day + timedelta(days = 2)
elif day.weekday() == 6:
    workingday = day + timedelta(days = 1)
else:
    workingday = day

print('Working day for',day,'is',workingday)

'''
=== FUNCTIONS === 02 ===
Working day for 2020-11-15 is 2020-11-16
'''

print('=== FUNCTIONS === 03 ===')

from datetime import date

def DaysTo31December():
    date_today = date.today()
    current_year = date_today.year
    date_end_year = date(current_year, 12, 31)
    delta = date_end_year - date_today
    print(delta.days)
    return

print('Days to 31st December:')
DaysTo31December()

'''
=== FUNCTIONS === 03 ===
Days to 31st December:
46
'''

print('=== FUNCTIONS === 04 ===')
print('How long you have already lived?')

from datetime import date

year = 1992
month = 5
day = 29

def HowLongYouLived():
    date_today = date.today()
    date_of_birth = date(year,month,day)
    delta = date_today - date_of_birth
    print(delta.days, 'days.')
    return 

HowLongYouLived() 

'''
=== FUNCTIONS === 04 ===
How long you have already lived?
10397 days.
'''

print('=== FUNCTIONS === 05 ===')
print('How long you have already lived?')

from datetime import date

def HowLongYouLived(year, month, day):
    date_today = date.today()
    date_of_birth = date(year,month,day)
    delta = date_today - date_of_birth
    print(delta.days, 'days.')
    return

HowLongYouLived(1992,5,29) 
HowLongYouLived(1994,8,5) 

'''
=== FUNCTIONS === 05 ===
How long you have already lived?
10397 days.
'''

print('=== FUNCTIONS === 06 ===')

def DoSth(price, item):
    print("price: ", price)
    print("item: ", item)
    return

DoSth('50','Backpack')
DoSth('70','BackpackXL')

print('----------------')

def DoSth(price, *item):
    print("price: ", price)
    print("item: ", item)
    return

DoSth('50','Backpack','BackpackXL','Boots')

'''
=== FUNCTIONS === 06 ===
price:  50
item:  Backpack
price:  70
item:  BackpackXL
----------------
price:  50
item:  ('Backpack', 'BackpackXL', 'Boots')
'''