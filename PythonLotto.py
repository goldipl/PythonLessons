import random

lottoNumbers = []

while len(lottoNumbers) <= 5:

    number = random.randint(1,49)

    #ochrona przed powtorzeniem numeru
    if number in lottoNumbers:
        print("Powtórzenie: ", number)
        continue

    lottoNumbers.append(number)

print("Lotto numbers: ", lottoNumbers)