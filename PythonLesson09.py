print("=== LOOPS === 01 ===")

i = 1
iMax = 10

while i <= iMax:
    print(i,"I love Python")
    i+=2
else:
    print("Now i = ", i)

'''
=== LOOPS === 01 ===
1 I love Python
3 I love Python
5 I love Python
7 I love Python
9 I love Python
Now i =  11
'''

print("\n=== LOOPS === 02 ===")

weight = [15,1,14,5,6,8,9,11,22,16,2,19,13]

print("The weight list is: ", weight)

weight.sort()
weight.reverse()

truckCapacity = 90
truck = []
i = 0

while sum(truck) + weight[i] < truckCapacity and i<len(weight):
    truck.append(weight[i])
    i+=1

print("The collected items sum is: ", sum(truck))
print("The elements: ", truck)

'''
=== LOOPS === 02 ===
The weight list is:  [15, 1, 14, 5, 6, 8, 9, 11, 22, 16, 2, 19, 13]
The collected items sum is:  86
The elements:  [22, 19, 16, 15, 14]
'''

print("\n=== LOOPS === 03 ===")

persons = ['Nowak', 'Bobak', 'Abak', 'Kabak', 'Dabak', 'Wabak']

domain = 'company.com'

for person in persons:
    email = person + '@' + domain
    print('Person:\t', person, '\tEmail:\t', email)
else:
    print("--- End of the list ---")

'''
=== LOOPS === 03 ===
Person:  Nowak  Email:   Nowak@company.com
Person:  Bobak  Email:   Bobak@company.com
Person:  Abak   Email:   Abak@company.com
Person:  Kabak  Email:   Kabak@company.com
Person:  Dabak  Email:   Dabak@company.com
Person:  Wabak  Email:   Wabak@company.com
--- End of the list ---
'''

print("\n=== LOOPS === 04 ===")

data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
 
for s in data:
    print(s.upper())
 
print('----------------')
 
for s in data:
    elements = s.split(':')
    print(elements[0].upper())
    print(elements[1])


'''
=== LOOPS === 04 ===
ERROR:FILE CANNOT BE OPEN
ERROR:NO FREE SPACE ON DISK
ERROR:FILE MISSING
WARNING:INTERNET CONNECTION LOST
ERROR:ACCESS DENIED
----------------
ERROR
File cannot be open
ERROR
No free space on disk
ERROR
File missing
WARNING
Internet connection lost
ERROR
Access denied
'''

print("\n=== LOOPS === 05 ===")

for number in range (2,15):
    print(number)

print('------------')

for number in range (2,15,2):
    print(number)

print('------------')

for number in range (2,15):
    if number %2 == 0:
        print('Number %2d is %s' % (number, 'even'))
    else:
        print('Number %2d is %s' % (number, 'odd'))

'''
=== LOOPS === 05 ===
2
3
4
5
6
7
8
9
10
11
12
13
14
------------
2
4
6
8
10
12
14
------------
Number  2 is even
Number  3 is odd
Number  4 is even
Number  5 is odd
Number  6 is even
Number  7 is odd
Number  8 is even
Number  9 is odd
Number 10 is even
Number 11 is odd
Number 12 is even
Number 13 is odd
Number 14 is even
'''

print("\n=== LOOPS === 06 ===")

for x in range (1,6):
    line = str(x)
    for y in range (1,6):
        line += ('\t%2d' % (x*y))
    print(line)

'''
=== LOOPS === 06 ===
1        1       2       3       4       5
2        2       4       6       8      10
3        3       6       9      12      15
4        4       8      12      16      20
5        5      10      15      20      25
'''