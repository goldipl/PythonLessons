print('==== OUTPUT-01 - DICTIONARY ====')

gamesBosses = {'D01':'Mefisto', 'D02':'Diablo'}

print(gamesBosses)
print(gamesBosses['D01'])
gamesBosses['D03'] = 'Duriel'
print(gamesBosses)
print(gamesBosses.get('D01'))
gamesBosses.update(D04 = 'Andariel', D05 = 'Baal')
print(gamesBosses)
print(gamesBosses.get('D05'))
print(gamesBosses.keys())
print(gamesBosses.values())
print(gamesBosses.items())

newBosses = {'D01':'ArcMefistox', 'D02':'ArcDiablox'}
gamesBosses.update(newBosses)
print(gamesBosses)

'''
==== OUTPUT-01 - DICTIONARY ====
{'D01': 'Mefisto', 'D02': 'Diablo'}
Mefisto
{'D01': 'Mefisto', 'D02': 'Diablo', 'D03': 'Duriel'}
Mefisto
{'D01': 'Mefisto', 'D02': 'Diablo', 'D03': 'Duriel', 'D04': 'Andariel', 'D05': 'Baal'}
Baal
dict_keys(['D01', 'D02', 'D03', 'D04', 'D05'])
dict_values(['Mefisto', 'Diablo', 'Duriel', 'Andariel', 'Baal'])
dict_items([('D01', 'Mefisto'), ('D02', 'Diablo'), ('D03', 'Duriel'), ('D04', 'Andariel'), ('D05', 'Baal')])
{'D01': 'ArcMefistox', 'D02': 'ArcDiablox', 'D03': 'Duriel', 'D04': 'Andariel', 'D05': 'Baal'}
'''