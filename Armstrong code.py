def armstrong(number):
    num_str=str(number)
    num_digits=len(num_str)
    total=sum(int(digit) **num_digits for digit in num_str)
    return total == number

num=int(input("Enter a Number"))
if armstrong(num):
    print(f"{num} is an armstrong")
else:
    print(f"{num} is not an armstrong")
