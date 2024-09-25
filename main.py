# print("hello world")
# a= ["je parle a petite francais"]
# b= ["la maison"]
# print(a + b)
#
from xml.etree.ElementTree import tostring


def printMe(i):
    print("Hello world! - ", i)

#loops
# for loop
def i_am_a_loop(data):
    for i in range(data):
        print("Hello world - ", i)

# i_am_a_loop(5)

#while loop
i = 1
while i <= 5:
    # print(i)
    i += 1

#condition statements
a = 2
b = 2

if( a > b):
    print("A is grater!")
elif(b > a):
    print("B is greater!")
else:
    print("A & B are equal!")

# nested if

if(a > 0):
    print("A is greater than Zero")
    if(a > b):
        print("A is greater than B!")
    elif (b > a):
        print("B is greater!")
    else:
        print("A & B are equal!")


#Hello World!