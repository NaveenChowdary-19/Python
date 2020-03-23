import datetime
from datetime import datetime , date
def addyears(d,years):
    try:
        return d.replace(year = d.year + years)
    except ValueError:
        #leap 
        return d+(date(d.year+years,1,1)-date(d.year,1,1))

string = input()
year_in_int = int(input())
date_obj = datetime.strptime(string,'%b %d %Y')
print(addyears(datetime.date(date_obj),year_in_int),end='')
