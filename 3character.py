def countDecoding(digit, x):
    count = [0] * (x+1) 
    count[0] = 1
    count[1] = 1
    for i in range(2, x+1):
        count[i] = 0
        if (digits[i-1] > '0'):
            count[i] = count[i-1]
         if (digits[i-2] == '1' or (digits[i-2] == '2' and digits[i-1] < '7') ):
            count[i] += count[i-2]
    return count[x]
digits = ['1','2','3','4']
x = len(digits)
print("Count is ",countDecoding(digits, x))
