# 10/2==0
def factors(num):
    if num < 1:
        return "Not a valid input"
    else:
        fac_list = [1]
        for i in range(2, num):
            if num%i==0:
                fac_list.append(i)
        return fac_list            
num = int(input("Enter a natural number: "))

print(factors(num))
            