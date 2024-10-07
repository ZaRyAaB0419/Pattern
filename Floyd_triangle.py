#taking input from user
rows = int(input("please enter the total number of rows : "))
number = 1 

print("Floyd's Triangle")
for i in range(1, rows + 1):
    for i in range(1, i +1):
        print(number, end = '     ')
        number = number + 1
    print()