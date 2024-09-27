# num = int(input("Enter the number required"))
# for i in range(0, num + 1):
#     print(i)

# l1 = [1,2,3,4]
# result = 0
# for i in l1:
#   result += i
# print("The Result is:", result)

# l2 = [1,2,3,4,5,6,7,8,9,0]
# for i in range(0, 10):
#   if i % 2 == 0:
#     print(i, end=' ')
# print()
# for i in range(0, 11):
#   if i % 2 == 0:
#     print(i, end=' ')
# print()
# for i in range(0, 10, 3):
#   if i % 2 == 0:
#     print(i, end=' ')

# d1 = {1:"name", 2:"roll number", 3:"dept"}
# for i in d1:
#     print(i, d1[i])
#
#
# for i in d1:
#     print(i, d1.get(i))

# for i in range(1,20):
#     for j in range(0, i):
#         if j%i:
#           print(j)
# print("prime")

# WHILE

# num = 7
# while num >= 7:
#     print(num)
#     break
# else:
#     print("number should be smaller that 7")

# num = 0
# while num<= 20:
#     num+=1
#     print(num)
# else:
#     print()

num = '0'
while num.isnumeric() == True:
    num = 'joel'
    if num.isnumeric() == True:
        print("incorrect")
    print("the input given is number")

# var = '0'
# while var.isnumeric() == True:
#    var = "test"
#    if var.isnumeric() == True:
#       print ("Your input", var)
# print ("End of while loop")