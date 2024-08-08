def checkPrimes(n):
    for i in range(2, n):
        
        for j in range(2, i):
            if i%j==0:
                print(f"{i}: Not Prime")
                break
        else:
            print(f"{i}: Prime")
    
checkPrimes(10)