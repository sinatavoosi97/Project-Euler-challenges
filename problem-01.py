# Multiples of 3 or 5
# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

i=1
multiple35=0
while 3*i<1000:

    multiple35+=3*i
    i+=1

i=1
while 5*i<1000:

    multiple35+=5*i
    i+=1


print(multiple35)