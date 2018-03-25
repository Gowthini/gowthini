def xxx(a,a_size):
    inv_count = 0
    if a_size < 2:
        print("Invalid Input")
        return
    min_x = 0
    min_y = 1
    min_sum = a[0] + a[1]
    for x in range (0, a_size - 1):
        for y in range (x + 1, a_size):
            sum = a[x] + a[y]                 
            if abs(min_sum) > abs(sum):         
                min_sum = sum
                min_x = x
                min_y = y
    print("The two elements whose sum is minimum are", 
            a[min_x], "and ", a[min_y])
a = [1, 67, -16, 7, -8, 8, 56]
 
xxx(a, 7);
