pattern = int(input('Enter the size of the pattern: '))

count = 0
while count != pattern:
    for i in range(pattern):
        if i == 3:
            print("*", end="\n")
        else:
            print("*", end="")
    count += 1