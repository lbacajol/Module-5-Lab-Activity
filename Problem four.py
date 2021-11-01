# Leslie Bacajol
# Date: 10/29/21
# This program shows numbers 1-50
# for multiples of three prints “Divisible by three” instead of the number
# for the multiples of five prints “Divisible by five”.
# For numbers which are multiples of both three and five prints “Divisible by both”

for i in range(1, 51):
    if i % 3 == 0:
        print("Divisible by three")
    elif i % 5 == 0:
        print("Divisible by five")
    elif i % 3 & 5 == 0:
        print("Divisible by both")
    else:
        print(i)
