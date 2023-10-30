def myFunc(arr):
    even = [] 
    odd = []

    for i in arr :
        if (i % 2 != 0) :
            odd.append(i)
        else:
            even.append(i)
    return f"Even numbers: {even} \nOdd numbers: {odd}" 

print(myFunc([1,7,10,11,22,37]))
