print('=== Input and Output Operators ===')

yourname = input("Enter your name: ")
print("Hello", yourname)

yoursurname = input("Enter your surname: ")
print("Surname: %s" % (yoursurname))

while True:

    yourage = input("Enter your age: ")

    if yourage.isdecimal():
        yourage = int(yourage)
        break
    else:
        print("Wrong type! Must be decimal!")
    
print("-------------------------------------------------")
print("Name: %s. Surname: %s. Age: %d." % (yourname, yoursurname, yourage))