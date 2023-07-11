#implement recursive factorial function with caching using a technique called memoization. 
#Memoization is a way to store previously computed results to avoid redundant calculations and improve the performance of recursive functions.


def factorial (x):
    if x == 1:
        return 1
    return factorial(x-1)*x
print(factorial(5))
