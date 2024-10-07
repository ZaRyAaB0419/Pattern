print("half pyramid pattern of stars(*):")
n = int(input("enter the number of rows:"))

for i in range(n):
    for i in range(i+1):
        print("* ", end="")
    print()
