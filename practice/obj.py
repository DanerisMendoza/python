obj = {'name':{'first-name':'john','last_name':'doe'},'age':18, 1:'number-one'}
print(obj['name']['first-name'])
print(obj['age'])
print(obj[1])
print('-------------')
print(obj.get('name').get('last_name'))
print(obj.get('age'))
print(obj.get(1))
print('-------------')
obj['gender'] = 'male'
print(obj['gender'])
print('-------------')
for i in obj:
    print(i)
print('-------------')
for key,val in obj.items():
    print(str(key)+"         "+str(val))