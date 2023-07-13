#Create a recursive function to find the sum of digits of a given positive integer.


def sum_d(digit):
    if digit == 0:
        return 0
    return sum_d(digit//10) + digit%10
print(sum_d(768))
