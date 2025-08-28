def odd():
    num=[]
    for i in range(5):
        number=int(input("enter number"))
        num.append(number)
    n=len(num)
    for i in range(n):
        for j in range(0,n-i-1):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
    print(num)
            
odd()    