print('------ OUTPUT1 ------')

message01 = 'File %s has size %d KB'
print(message01 % ('text_file.txt', 40))

message02 = 'File = %s'
print(message02 % ('text_file.txt'))

message03 = 'File %20s has size %5d MB'
print(message03 % ('text_file.txt', 404))

message04 = 'Processing file {0:s}'
print(message04.format('text_file.txt'))

message05 = 'Processing file {0:s} has size {1:d}'
print(message05.format('text_file.txt', 40))

message06 = 'Processing file {1:s} has size {0:d}'
print(message06.format(40, 'text_file.txt'))

message07 = 'Processing file {1:20s} has size {0:20d}'
print(message07.format(40, 'text_file.txt'))
print('')

'''
------ OUTPUT1 ------
File text_file.txt has size 40 KB
File = text_file.txt
File        text_file.txt has size   404 MB
Processing file text_file.txt
Processing file text_file.txt has size 40
Processing file text_file.txt has size 40
Processing file text_file.txt        has size                   40
'''

print('------ OUTPUT2 ------')

helloMessage = "Hello %s!"
print(helloMessage % ('Marcin'))
print(helloMessage % ('Adam'))

helloMessage02 = "Hello {0:s}!"
print(helloMessage02.format('Marcin'))
print(helloMessage02.format('Adam'))

helloMessage03 = "%s has %d %s"
print(helloMessage03 % ('Marcin', 28, 'years.'))

helloMessage03 = "{0:s} has {1:d} {2:s}"
print(helloMessage03.format('Marcin', 28, 'years.'))

line = "{0:20s} costs {1:6f} €"
print(line.format('PIZZA', 6))
print(line.format('ICE CREAM', 1))
print(line.format('APPLE', 0.2))

'''
------ OUTPUT2 ------
Hello Marcin!
Hello Adam!
Hello Marcin!
Hello Adam!
Marcin has 28 years.
Marcin has 28 years.
PIZZA                costs 6.000000 €
ICE CREAM            costs 1.000000 €
APPLE                costs 0.200000 €
'''