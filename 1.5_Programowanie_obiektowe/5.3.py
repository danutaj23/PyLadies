# Napisz funkcję, która policzy BMI "Człowieka" (count_bmi).


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
            print('Kłamie, bo mogę')

    def recive_bribe(self):
        self.bribed = True


adam = Czlowiek('Adam', 1.80, 120)
ewa = Czlowiek('Ewa', 1.65, 60)

print(adam.wzrost)
print(adam.waga)
print(adam.bmi)
print(ewa.wzrost)
print(ewa.waga)
print(ewa.bmi)
