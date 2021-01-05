counter = 1
n = 1000000000000000000

while counter < n+1:

    if counter % 6 == 0:
        print(counter)
    else:
        print("\033[1;32;40m", counter, end=" ") #Change this line to print counter, for python version 2
    counter += 1
