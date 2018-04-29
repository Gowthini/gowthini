def HCF(m, n):
    if m > n:
        small = n
    else:
        small = m
    for i in range(1, small+1):
        if((m % i == 0) and (n % i == 0)):
            hcf = i
    return hcf
j =int(input("Enter first number")) 
k=int(input("Enter second number")) 
print(HCF(j,k))
