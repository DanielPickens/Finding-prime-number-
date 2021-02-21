
## this program checks whether a number is a prime number



num = 501
 
# If given number is greater than 1

if num > 1:
 

    # Iterate from 2 to Prime_num/ 2

    for i in range(2, num):
 

        # If num is divisible by any number between

        # 2 and Prime_num / 2, it is not prime

        if (num % i) == 0:

            print(num, "is not a prime number")

            break

    else:

        print(num, "is a prime number")
 

else:

    print(num, "is not a prime number")
