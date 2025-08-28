def square_table(num):
    square=num**2
    for i in range (1,11):
        print(f"{i} x {square}={i*square}")
square_table(int(input("enter the number: ")))

def multable(nm):
    for i in range(1,11):
        print(f"{i} x {nm} ={i*nm}")
multable(int (input("enter the number: ")))    