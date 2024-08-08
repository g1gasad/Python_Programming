def gcd(a, b):
    
    is_gcd = False
    result = min(a, b)
    while not is_gcd:
        if a%result==0 and b%result==0:
            is_gcd = True
            return result
        result -= 1
    return result

if __name__=="__main__":
    a = 22
    b = 36
    print(f"the gcd of numbers {a} and {b} is {gcd(a, b)}.\n")
