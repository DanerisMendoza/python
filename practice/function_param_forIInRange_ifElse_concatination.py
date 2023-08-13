def printN(n):
    for i in range(n): 
        if i%2 == 0:
            print("even: ",i)
        else:
            print("odd:  ",i)
    print("the value of n:",n,'is ten')

printN(10)