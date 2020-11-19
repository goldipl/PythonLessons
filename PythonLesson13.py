print('=== OS Path Module ===')

import os
import time

#funkcja os.getcwd() zwraca informacje o biezacym katalogu
print("Obecna lokalizacja = ", os.getcwd())

#wydruk do konsoli pelnej sciezki 
currDir = os.getcwd()
fileName = 'PythonLesson13.py'
fPath = os.path.join(currDir, fileName)
print(fPath)

#zwraca to samo co powyzej
relPath = 'PythonLesson13.py'
print(os.path.abspath(relPath))

#####inne#####

#zwroci PythonLesson13.py
print(os.path.basename(relPath))
#zwraca, czy dany plik/katalog istnieje
print(os.path.exists(relPath))
#zwraca czas modyfikacji
print(time.localtime(os.path.getmtime(fPath)))