print('==== OUTPUT-01 - LISTS ====')

flags = ['PL', 'DE', 'UK', 'RU']
print(flags[1])
flags[1] = 'GB'
print(flags)
flags.append('DE')
print(flags)
flags.insert(2, 'ES')
print(flags)
flags.remove("ES")
print(flags)
flags.sort()
print(flags)
flags.reverse()
print(flags)
print(flags.pop(2))
print(flags)
print(flags.index('GB'))

newFlags = ['SE', 'FI']
flags.extend(newFlags)
print(flags)

flagsCopy = flags.copy()
flagsCopy.clear()
print(flags)
print(flagsCopy)

'''
==== OUTPUT-01 - LISTS ====
DE
['PL', 'GB', 'UK', 'RU']
['PL', 'GB', 'UK', 'RU', 'DE']
['PL', 'GB', 'ES', 'UK', 'RU', 'DE']
['PL', 'GB', 'UK', 'RU', 'DE']
['DE', 'GB', 'PL', 'RU', 'UK']
['UK', 'RU', 'PL', 'GB', 'DE']
PL
['UK', 'RU', 'GB', 'DE']
2
['UK', 'RU', 'GB', 'DE', 'SE', 'FI']
['UK', 'RU', 'GB', 'DE', 'SE', 'FI']
[]
'''

print('==== OUTPUT-02 - TUPLES (STATIC LISTS) ====')

price = (5, 10, 18, 99)
print(price)
print(price[0])
print(price.index(5))
print(price.count(99))
print(max(price))

#price.reverse() - we can't do this! Tuple = static list!
priceList = list(price)
priceList.reverse()
print(priceList)
priceList.append(140)
print(priceList)
priceList = tuple(priceList)
print(priceList)

'''
==== OUTPUT-02 - TUPLES (STATIC LISTS) ====
(5, 10, 18, 99)
5
0
1
99
[99, 18, 10, 5]
[99, 18, 10, 5, 140]
(99, 18, 10, 5, 140)
'''

print('==== OUTPUT-03 - TUPLES (STATIC LISTS) ====')

x = 10
y = 20
print("x = ",x, "\ty = ",y)
#tmp = x
#x = y
#y = tmp
(x,y) = (y,x)
print("x = ",x, "\ty = ",y)

'''
==== OUTPUT-03 - TUPLES (STATIC LISTS) ====
x =  10         y =  20
x =  20         y =  10
'''