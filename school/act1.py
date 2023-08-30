# 36 and 10 (*inputted val)
input1 = int(input("Input a value for num 1: "))
input2 = int(input("Input a value for num 2: "))
maxVal = 0
lowVal = 0 
if(input1 >= input2):
    maxVal = input1
    lowVal = input2
else:
    maxVal = input2
    lowVal = input1
print("max: "+ str(maxVal))
print("low: "+ str(lowVal))
quotient = product = 0
for i in range(maxVal):
    if(product < maxVal and (product+lowVal) <= maxVal):
        quotient += 1
        product += lowVal
modulo = maxVal - product
print("quotient: "+str(quotient))
print("product: "+str(product))
print("modulo: "+str(modulo))