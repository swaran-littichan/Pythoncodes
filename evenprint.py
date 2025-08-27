def print_even(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i,end=" ")

print_even(2, 10)