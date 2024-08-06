# 10/2==0
def factors(num):
    fac_list = [1]
    for i in range(2, num-1):
        if num%i==0:
            fac_list.append(i)
    return fac_list            
num = int(input("Enter a natural number: "))

print(factors(num))
            