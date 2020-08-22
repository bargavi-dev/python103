num_of_rows = int(input('How many rows would you like? '))


for i in range(1, num_of_rows):
    for j in range(num_of_rows - i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print()