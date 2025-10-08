#old style of output formating-using comma
name = "Ravi"
age = 20
print("Name is", name, " and age is", age)

#Modulo operator
##Access Specifiers
#%d - Integers
#%f - float
#%s - String

name = "Ravi"
age = 20
print("Name is %s and age is %d"%(age,name))


#Dot format
name = "Ravi"
age = 20
print("Name is {} and age is {}".format(name,age))
print("Name is {} and age is {}".format(age,name))
print("Name is {1} and age is {0}".format(name,age+5))


#f-format
name = 'Ravi'
age = 20
percentage = 95.2568
print(f"Name is (name) and age is (age) and i have {percentage}")
print(f"Name is (name) and age is (age) and i have {percentage:2f}")
num = '01'
print(int(num))
