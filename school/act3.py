creditCardNum = "4624 7482 3324 9080"
# print(creditCardNum[19])
for i in range(len(creditCardNum)-1, -1, -2):
    # print(creditCardNum[i])
    if(creditCardNum[i-1] == " "):
        continue
    print(creditCardNum[i-1])
    # print(creditCardNum[i-1])