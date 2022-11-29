import datetime #importing date and time module
now = datetime.datetime.now() # assign a value to display that
print ("Current date and time : ") 
print (now.strftime("%Y-%m-%d %H:%M:%S"))