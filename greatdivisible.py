def HCF(m, n):
    if m > n:
        smaller = n
    else:
        smaller = m
    for i in range(1, smaller+1):
        if((m % i == 0) and (n % i == 0)):
            hcf = i
    return hcf
x =int(input("Enter first number")) 
y = int(input("Enter second number")) 
print(HCF(x,y))
