# Napisz funkcję, która policzy BMI "Człowieka" (count_bmi).
# WZÓR: waga / (wzrost **2)      # wzrost w metrach (1.77)


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
        pass

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

print(adam.waga)
print(adam.wzrost)
print(adam.bmi)
