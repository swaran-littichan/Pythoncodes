def seven():
    num=[int(input("enter number: ")) for _ in range(7)]
    avg=sum(num)/len(num)
    minimum=min(num)
    print("Average: ",avg)
    print("minimum:",minimum)
seven()