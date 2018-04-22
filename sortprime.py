x=int(input("Enter an integer:"))
print("Factors are:")
s=1
while(s<=x):
    m=0
    if(x%s==0):
        j=1
        while(j<=s):
            if(s%j==0):
                m=m+1
            j=j+1
        if(m==2):
            print(s)
    s=s+1
