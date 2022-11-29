from datetime import date

start_year=int(input("Please enter a year of start: "))
start_month=int(input("Please enter a month of start: "))
start_day=int(input("Please enter a day of start: "))
last_year=int(input("Enter finish year: "))
last_month=int(input("Enter finish month: "))
last_day=int(input("Enter finish day: "))
start = date(start_year, start_month, start_day)
last = date(last_year, last_month, last_day)
print("The difference is: ", last-start)