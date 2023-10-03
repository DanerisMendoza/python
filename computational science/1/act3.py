creditCardNum = "4624 7482 3324 9080"
counter = counter2 = len(creditCardNum)
result = result2 = digitsOfResultArr = digitsOfResultArr2 = []
digitsOfResult = digitsOfResult2 = ""
sum = sum2 = 0

while(counter > 0):
    #block of getting every other digits starting from right to left
    if(creditCardNum[counter-1] == " "):     # add extra 1 counter if encounter whitespace or add 1 move for another position
        counter-=1
    result += (creditCardNum[counter-2]) 
    print(creditCardNum[counter-2])
    counter -= 2    #move to other 2 position

    # remaining
    # if(creditCardNum[counter2-2] == " "):     
    #     counter2-=1
    # result2 += (creditCardNum[counter2-1]) 
    # counter2 -= 2


for i in range(len(result)):
    res = int(result[i])*2
    digitsOfResult += str(res)
    print(result[i] +"*2 = "+ str(res))

digitsOfResultArr = [int(i) for i in digitsOfResult]
for i in range(len(digitsOfResultArr)):
    sum += digitsOfResultArr[i]

for i in creditCardNum :
    if(i != " " and i not in result):
        print(i)

# print(sum)
# print("every other digits starting from right to left: "+ str(result))
# print(digitsOfResult)
print(result)
print(result2)
