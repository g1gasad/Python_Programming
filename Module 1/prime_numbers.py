def checkPrimes(n):
    for i in range(2, n+1):
        for j in range(2, i):
            if i%j==0:
                print(f"Not Prime | {i} equal {j} * {i//j}")
                break
        else:
            print(f"{i}: Prime")
    
checkPrimes(20)