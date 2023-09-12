arr = []
obj = {}
for i in range(5):
    i = input("Enter a number: ")
    arr.append(i)

# for i in arr:
#     if i in obj:
#         obj[i] += 1
#     else:
#         obj[i] = 1

for i in range(len(arr)):
    if arr[i] in obj:
        obj[arr[i]] += 1
    else:
        obj[arr[i]] = 1

for key,value in obj.items():
    print(str(key)+" "+str(value))
    