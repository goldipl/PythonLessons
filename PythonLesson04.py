print('==== OUTPUT-01 ====')
x = "Python jest super!"
print (x[0])
print (x[1])
print (x[:6])
print (x[6:])
print (x[222:999])
print (x[2:999])

'''
==== OUTPUT-01 ====
P
y
Python
 jest super!

thon jest super!
'''

print('==== OUTPUT-02 ====')
msg = 'File "folder" was made on computer: COMP-01'
print(msg.find(':'))
print(msg[msg.find(':'):])
print(msg[msg.find(':')+2:])
print(msg[msg.find('"')+1:])
tmp = msg[msg.find('"')+1:]
print(tmp[:tmp.find('"')])

'''
==== OUTPUT-02 ====
34
: COMP-01
COMP-01
folder" was made on computer: COMP-01
folder
'''