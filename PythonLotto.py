import random

lottoNumbers = []

while len(lottoNumbers) <= 5:

    number = random.randint(1,49)

    #ochrona przed powtorzeniem numeru
    if number in lottoNumbers:
        print("Powtórzenie: ", number)
        continue

    lottoNumbers.append(number)

#konwersja tablicy do str
stringLottoNumbers = ' '.join(str(e) for e in lottoNumbers)

print("Lotto numbers: ", stringLottoNumbers)