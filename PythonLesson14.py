print('=== Input/Output Text Files ===')

# literka "r" oznacza plik otwarty do odczytu /read
file = open("C:\\Users\\Marcin\\Desktop\\file.txt", "r")

content = file.read()
print(content)

file.close()

#to samo co wyzej, lecz bez koniecznosci zamykania
#nie trzeba pamietac o zamykaniu pliku
with open("C:\\Users\\Marcin\\Desktop\\file.txt", "r") as file:
    content = file.read()
    print(content)

#to samo co wyzej, lecz linijka po linicje -> dla duzych plikow
with open("C:\\Users\\Marcin\\Desktop\\file.txt", "r") as file:
    for line in file:
        print(line)

print('--------------Write To File--------------')

file = "C:\\Users\\Marcin\\Desktop\\file.txt"

numbers = ['one','two','three','four','five']
line = 'Ala ma kota'

# otwieramy plik do zapisu "w" /write ---- append 'a' dopisywanie do pliku
# "w+" oznacza do zapisu i do odczytu
file = open(file, "w")
file.write(line)
file.write('\n')

for number in numbers:
    file.write(number + ' ')

print(file)

file.close()