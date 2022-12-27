# Program to input two numbers find the larger/smaller number
def isGreater(a,b):
    if(a>b):
        Large = a
        print("Larger number is :", Large)
    else:
        Large = b
        print("Larger number is :", Large)
    if(Large==a):
        print("Smaller number is :", b)
    else:
        print("Smaller number is :", a)

a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))

isGreater(a,b)
