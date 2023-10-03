obj = {'digits':0,'letter':0}
sentence = input("Input Sentece: ")
for i in range(len(sentence)):
    if sentence[i].isdigit():
        obj['digits'] +=1
    if sentence[i].isalpha():
        obj['letter'] +=1
print(obj)