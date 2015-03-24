#this is an Example of Indexing operation of python(24.03.15)
months = ['january','February','March','April','May','Jun','July','August','september','october','november','december']
#a list wiht one ending for each number from 1 to 31
ending = ['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
year = raw_input('Year: ')
month = raw_input('Month (1-12)')
day = raw_input('Day (1-31)')
month_name = months[int(month)-1]
ordinal = day + ending[int(day)-1]
print month_name+ ' '+ordinal +','+year
