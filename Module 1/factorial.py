def factorial(n):
    out = 1
    while n>1:
        out = out * n
        n = n - 1
    return out

def rec_factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n * rec_factorial(n-1)

if __name__=="__main__":
    n = 4
    print(f"the factorial of {n} is {rec_factorial(n)}")