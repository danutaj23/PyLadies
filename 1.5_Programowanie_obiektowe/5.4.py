# Napisz funkcję, która policzy, ile kilogramów brakuje do normy (diff_to_norm).
# niedowaga = 18.5, nadwaga = 25.0
# na bazie nadwaga lub niedowaga:
# oczekiwana waga = bmi *(wzrost **2)


class Czlowiek:

    def __init__(self, imie, wzrost, waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga
        self.bmi = self.count_bmi()


    def speak(self):
        print('Mówię prawdę.')

    def count_bmi(self):
        bmi = self.waga/(self.wzrost**2)
        return bmi

    def diff_to_norm(self):
        if self.bmi < 18.5:
            oczekiwana_waga = 18.5 * self.wzrost ** 2
            roznica = oczekiwana_waga - self.waga
            print('Musisz przytyć {} kg.'.format(roznica))
        elif self.bmi > 25:
            oczekiwana_waga = 25.0 * self.wzrost ** 2
            roznica = self.waga - oczekiwana_waga
            print(('Musisz schudnąć {} kg.'.format(roznica)))
        else:
            print('Waga w normie.')

    def save_data(self):
        pass

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
            print('Kłamię, bo mogę!')

    def recive_bribe(self):
        self.bribed = True


anna = Czlowiek('Anna', 1.65, 60)
adam = Czlowiek('Adam', 1.90, 120)

print(anna.waga)
print(anna.wzrost)
print(anna.bmi)
anna.diff_to_norm()

print(adam.waga)
print(adam.wzrost)
print(adam.bmi)
adam.diff_to_norm()
