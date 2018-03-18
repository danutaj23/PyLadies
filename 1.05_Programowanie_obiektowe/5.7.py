# Zakładając, że aby przytyć 1 kg trzeba dostarczyć 6000kcal, napisz funkcjonalność,
# która powie użytkownikowi, ile powinien zjeść czekolady(450kcal/100g) / ziemniaków(80kcal/100g)
# więcej aby być w normie (to_eat)


import json


class Czlowiek:
    def __init__(self, imie, wzrost, waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga
        self.bmi = self.count_bmi()

    def speak(self):
        print('Mowie prawdę')

    def count_bmi(self):
        bmi = self.waga / (self.wzrost ** 2)
        return bmi

    def diff_to_norm(self):
        if self.bmi < 18.5:
            oczekiwana_waga = 18.5 * self.wzrost ** 2
            roznica = oczekiwana_waga - self.waga
            return roznica
        elif self.bmi > 25:
            oczekiwana_waga = 25.0 * self.wzrost ** 2
            roznica = self.waga - oczekiwana_waga
            return roznica
        else:
            return 0

    def save_data(self):
        with open('{}.json'.format(self.imie), 'w') as file:
            json.dump(
                {
                    'imie': self.imie,
                    'wzrost': self.wzrost,
                    'waga': self.waga,
                    'bmi': self.bmi
                },
                file
            )

    def to_burn(self, aktywnosc):
        kcal = self.diff_to_norm() * 6000
        if aktywnosc == 'bieganie':
            return kcal / 500
        elif aktywnosc == 'rower':
            return kcal / 600
        elif aktywnosc == 'hobby':
            return kcal / 250
        elif aktywnosc == 'szachy':
            return kcal / 150
        else:
            return 'Wybierz inną aktywność'

    def to_eat(self, jedzenie):
        kcal = self.diff_to_norm() * 6000
        if jedzenie == 'czekolada':
            return kcal * (450/100)
        elif jedzenie == 'pyry':
            return kcal * (80/100)
        else:
            return "Zjedz coś innego"

    def what_to_do(self):
        pass


class Polityk(Czlowiek):
    bribed = False

    def speak(self):
        if self.bribed:
            super().speak()
        else:
            print('Kłamie, bo mogę')

    def recive_bribe(self):
        self.bribed = True


adam = Polityk('adam', 1.80, 120)
ewa = Czlowiek('ewa', 1.65, 60)
anna = Czlowiek('anna', 1.70, 50)

print(anna.diff_to_norm())
print(anna.to_eat('pyry'))
print(anna.to_eat('sałata'))
