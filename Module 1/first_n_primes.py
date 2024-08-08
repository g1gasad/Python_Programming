def prime_list(n):
    
    plist = []
    

    for i in range(2, n):
        for j in range(2, i):
            if i%j==0:
                # print(f"{i}: not prime")
                break
        else:
            # print(f'{i}: prime')
            plist.append(i)
            
    return plist

if __name__=="__main__":
    n = 100
    print(prime_list(n))