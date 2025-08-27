def odd_sum(end):
    sum=0
    for i in range(1,end+1):
        if i %2 !=0:
            sum=sum+1
    print(sum)
odd_sum(20)