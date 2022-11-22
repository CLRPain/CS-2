def factorial(n):
    if n < 0:
        return 'Negative Number'
    if n == 1: #base case
        return n
    return(n*factorial(n-1)) # 5*factorial(5-1 = 4) then 4* fac(3) until 2* fac(1) then recursion ends

print(factorial(1))