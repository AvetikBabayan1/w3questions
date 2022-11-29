#program to get the user name and lastname and print in reverse order
name= input("Enter your name: ")
lastname = input("Enter the lastname: ")
print(name[::-1], lastname[::-1]) #Function helps to write in reverse order the string

#program to get the filename and separate the file extension

filename = input("Please enter the filename and extension: ")

splitted = filename.split(".") #splitting by the filename usual separator
print (splitted[1]) #displaying the second element of the list containing file name and extension