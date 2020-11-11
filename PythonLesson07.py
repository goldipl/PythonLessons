print('==== CONDITIONAL STATEMENTS ====')

print('----- age = 28 --------')
age = 28

if age >= 18:
    print("You are adult and you can buy alcohol")
elif age < 18:
    print("You are too young to drink alcohol!")

print('------ age = 15 -------')
age = 15

if age >= 18:
    print("You are adult and you can buy alcohol")
elif age < 18:
    print("You are too young to drink alcohol!")

print('------ age = 30 & isDrunk -------')
age = 30
isDrunk = True

if age >= 18 and not isDrunk:
    print("You are adult and you can buy alcohol")
else:
    print("We cannot sell you alcohol!")

print('------ age = 40 & isDrunk -------')
age = 40
isDrunk = True

if age < 18:
    print("You are too young to drink alcohol!")
elif isDrunk:
    print("We cannot sell you alcohol! You are drunk!")
elif not isDrunk and age >= 18:
    print("You can buy alcohol ;-)")

print('------ age = 40 & is Not Drunk -------')
age = 40
isDrunk = False

if age < 18:
    print("You are too young to drink alcohol!")
elif isDrunk:
    print("We cannot sell you alcohol! You are drunk!")
elif not isDrunk and age >= 18:
    print("You can buy alcohol ;-)")

print('------ age = 16 & is Not Drunk -------')
age = 16
isDrunk = False

if age < 18:
    print("You are too young to drink alcohol!")
elif isDrunk:
    print("We cannot sell you alcohol! You are drunk!")
elif not isDrunk and age >= 18:
    print("You can buy alcohol ;-)")

'''
==== CONDITIONAL STATEMENTS ====
----- age = 28 --------
You are adult and you can buy alcohol
------ age = 15 -------
You are too young to drink alcohol!
------ age = 30 & isDrunk -------
We cannot sell you alcohol!
------ age = 40 & isDrunk -------
We cannot sell you alcohol! You are drunk!
------ age = 40 & is Not Drunk -------
You can buy alcohol ;-)
------ age = 16 & is Not Drunk -------
You are too young to drink alcohol!
'''