#Justin Mitchell 2/14/2021
#Program uses the range to find the numbers that are divisible by 3,5, and both. Prints out the answers as well.

for n in range(50):
    if n % 5==0:
        if n % 3==0:
            print (n, "Divisible by both 3 and 5")

    elif n % 5==0:
            print (n, "Divisible by 5")

    elif n % 3==0:
            print (n, "Divisble by 3")

