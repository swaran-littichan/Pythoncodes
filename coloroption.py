def color(num):
    if 0<=num<50:
        print("Yellow")
    elif 50<=num<100:
        print("blue")
    elif 100<=num<200:
        print("Red")
    else:
        print("not in colour option")
color(int(input("enter a number")))