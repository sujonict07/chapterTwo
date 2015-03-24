tag = '<a herf="http://www.python.org">python web site</a>'
print tag[9:30]
print tag[32:-4]
numbers = [1,2,3,4,5,6,7,8,9,10]
for idx, val in enumerate(numbers):
    print idx, val
print numbers[1:10]
print numbers[0:9:3] # last index means the deference value to be printed.
print numbers[10:0:-1] # total element (8-3) = 5, difference 1, sorting desending order
#adding sequence 
print tag+"this is adding"
print numbers +[1,11,2,15]
#Multiplication
print 'python '*5
print [54]*5