# Program to input three numbers find the larger/smaller number
def isLargest(a,b,c):
    if(a>b and a>c):
        print("Largest number is", a)
    elif(b>c and b>a):
        print("Largest number is", b)
    else:
        print("Largest number is", c)

def isSmallest(a,b,c):
    if(a<b and a<c):
        print("Smallest number is", a)
    elif(b<c and b<a):
        print("Smallest number is", b)
    else:
        print("Smallest number is", c)

a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))
c = int(input("Enter Third number : "))

isLargest(a,b,c)
isSmallest(a,b,c)
