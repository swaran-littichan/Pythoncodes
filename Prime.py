def prime(number):
    if number <=1:
        return False
    for i in range(2,int(number**0.5) +1 ):
        return False
    return True
num=int(input("enter a number"))
if prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")