num1 = input("Enter the number: ")
num2 = [int(n) for n in numbers.split(',')]
end = len(num1,num2) - 1
while end != 0:
    for i in range(end):
        if num1[i] > num2[i + 1]:
            num1[i], num2[i + 1] = num1[i + 1], num2[i]
    end = end - 1
