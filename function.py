# def printme(joe):
#     print(joe)
#     return
# printme ("j'aime le paris")

# def printme(joe):
#     joe = "ouais"
# print("joe")
# # printme ("j'ai")

def testfunction(arg):
   print ("ID inside the function:", id(arg))
   arg = arg + 1
   print ("new object after increment", arg, id(arg))

var=10
print ("ID before passing:", id(var))
testfunction(var)
print ("value after function call", var)