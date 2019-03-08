# divya
Repository for python practice


"""
def changeme( mylist,val ):
   "This changes a passed list into this function"
   mylist.append(1)
   mylist.append(2)
   mylist.append(3)
   myval = val + 1
   print ("Values inside the function: ", mylist, myval)
   return myval, mylist

# Now you can call changeme function
mylist = [10,20,30]
myval = 25
print ("Values outside the function: ", mylist, myval)
changeme( mylist, myval )
print ("2 Values outside the function: ", mylist, myval)

op1, op = changeme(mylist, myval)
print(op)
print(op1)

"""
import random

list1 = [10,20,30,40,50]
for i in range(1,10):
    print(random.choice(list1))


def myfunc(*args, **kwargs):
	for x in args:
		print(x)
	for x, y in kwargs.items():
		print(y)

myfunc(2,"radha", 56, first="rk", second="krishna")
val1 = int(input("Please enter value 1: "))
val2 = int(input("Please enter value 2: "))

print(val1+val2)
