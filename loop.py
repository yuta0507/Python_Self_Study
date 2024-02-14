##### Basic(List)
print('## Basic(List) ##')

num_list = [1, 2, 3, 4, 5]

for i in num_list:
    print(i)

##### Basic(Dictionary)
print('## Basic(Dictionary) ##')

dinner = {'dish': 'pasta', 'drink': 'wine'}

for key, val in dinner.items():
    print(key, val)

##### Range A
print('## Range A ##')

for i in range(5):
    print(i)

##### Range B
print('## Ranage B ##')

for i in range(1, 5):
    print(i)

##### Enumerate
print('## Enumerate ##')

for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

##### Zip
print('## Zip ##')

days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'coke']

for days, fruits, drinks in zip(days, fruits, drinks):
    print(days, fruits, drinks)
