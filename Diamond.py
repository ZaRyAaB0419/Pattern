#take input from user
rowsize = int(input("enter the number of rows:"))
if rowsize%2==0: #conditions
    halfdiamrow = int(rowsize/2)
else:
    halfdiamrow = int(rowsize/2)+1
space = halfdiamrow-1
#loop for upper part
for i in range(1, halfdiamrow+1): #loop for rows
    for j in range(1, space+1): #loop for columns
        print(end=" ")
    space= space-1
    num = 1
    for j in range(1, 2*i-1):
        print(end=str(num))
        num=num+1

    print()
space=1

for i in range(1, halfdiamrow): #loop for rows
    for j in range(1, space+1): #loop for columns
        print(end=" ")
    space= space+1
    num = 1
    for j in range(1, 2*(halfdiamrow-i)):
        print(end=str(num))
        num=num+1

    print()