# Zaimplementuj zapisywanie JSON z danymi danego "Człowieka"
# na dysk pod plikiem <imie>.json (save_data).

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
            print('Musisz przytyć {} kg'.format(roznica))
        elif self.bmi > 25:
            oczekiwana_waga = 25.0 * self.wzrost ** 2
            roznica = self.waga - oczekiwana_waga
            print(('Musisz schudnąć {} kg'.format(roznica)))
        else:
            print('Waga w normie')

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

    def to_burn(self):
        pass

    def to_eat(self):
        pass

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

print(adam.bmi)
adam.save_data()

print(ewa.bmi)
ewa.save_data()
