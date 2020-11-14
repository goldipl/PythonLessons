print('=== TYPES === 01 ===')

num01 = 3.14342432
num02 = -4.6533634

print(num01, num02)
print(abs(num01), abs(num02))
print(round(num01), round(num02))
print(min(num01,num02), max(num01,num02))

list = [1,2,3,4,5,6,7,8,9]

print(sum(list), len(list))
print(sum(list)/len(list))
print(round(2.67898, 2))

'''
=== TYPES === 01 ===
3.14342432 -4.6533634
3.14342432 4.6533634
3 -5
-4.6533634 3.14342432
45 9
5.0
2.68
'''

print('=== TYPES === 02 ===')

percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
           8.740978348,6.174819567]
 
countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
             'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
             'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
             'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
             'Cyprus','Italy']
 
sumOfPoints = 4988
 
print('min', min(percent), 'max', max(percent))
 
for i in range(len(countries)):
 
    print(percent[i], int(percent[i]), round(percent[i],2), int(round(percent[i]*sumOfPoints/100,0)), countries[i])

'''
=== TYPES === 02 ===
min 0.781876504 max 10.60545309
2.606255012 2 2.61 130 Ukraine
1.222935044 1 1.22 61 Spain
1.283079391 1 1.28 64 Slovenia
3.628708901 3 3.63 181 Lithuania
6.856455493 6 6.86 342 Austria
4.911788292 4 4.91 245 Estonia
2.886928629 2 2.89 144 Norway
0.781876504 0 0.78 39 Portugal
0.962309543 0 0.96 48 United Kingdom
2.265437049 2 2.27 113 Serbia
6.816359262 6 6.82 340 Germany
3.688853248 3 3.69 184 Albania
3.468323978 3 3.47 173 France
5.633520449 5 5.63 281 Czech Republic
4.530874098 4 4.53 226 Denmark
1.984763432 1 1.98 99 Australia
0.922213312 0 0.92 46 Finland
3.327987169 3 3.33 166 Bulgaria
4.190056135 4 4.19 209 Moldova
5.493183641 5 5.49 274 Sweden
1.864474739 1 1.86 93 Hungary
10.60545309 10 10.61 529 Israel
2.425821973 2 2.43 121 Netherlands
2.726543705 2 2.73 136 Ireland
8.740978348 8 8.74 436 Cyprus
6.174819567 6 6.17 308 Italy
'''

print('=== TYPES === 03 ===')

# importujemy modul math :) 
import math
print(math.pi)
# importujemy wszystkie funkcje z modulu math :) 
from math import *
print(pi)
print(floor(pi))

'''
=== TYPES === 03 ===
3.141592653589793
3.141592653589793
3
'''

print('=== TYPES === 04 ===')

# importujemy modul math :) 
import math

num01 = 3.14342432
num02 = -4.6533634

print(math.ceil(num01))
print(math.ceil(-num01))
print(math.floor(num01))
print(math.floor(-num01))
print(math.pow(2,8))
print(math.sqrt(16))
print(math.pi)
print(math.e)
print(math.sin(math.pi/2))

deg = 360
rad = deg * math.pi / 180
print("%d degree is %f radians" % (deg, rad))

'''
=== TYPES === 04 ===
4
-3
3
-4
256.0
4.0
3.141592653589793
2.718281828459045
1.0
360 degree is 6.283185 radians
'''

print('=== TYPES === 05 ===')
print('====== RANDOM ======')

import random

print('Random numer: ', random.randint(1,100))
print('Random numer: ', random.randrange(1,100))
print('Random number from 1 to 100')

list = ['Adam', 'Marcin', 'Damian', 'Anna', 'Ola']
random.shuffle(list)
print(list)
print('Random list')

for i in range(10):
    print(random.randint(1,100))
print('Random 10 number from 1 to 100')

'''
=== TYPES === 05 ===
====== RANDOM ======
Random numer:  1
Random numer:  68
Random number from 1 to 100
['Ola', 'Marcin', 'Anna', 'Adam', 'Damian']
Random list
89
60
50
95
51
43
27
91
21
85
Random 10 number from 1 to 100
'''