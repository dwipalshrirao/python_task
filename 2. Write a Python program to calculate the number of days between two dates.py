import datetime


try:
    a=int(input('enter 1st date'))
    b=int(input('enter 2nd date'))
    
except ValueError:
    print('input date must be in number fprmat')

try:
    difference=(datetime.datetime.strptime(str(a),'%Y%m%d')- datetime.datetime.strptime(str(b),'%Y%m%d')).days
    c= -difference if difference < 0 else difference
    print('difference between 2 date is ',c)
except ValueError:
    print('please provide valid date')