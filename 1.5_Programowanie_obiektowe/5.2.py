# Stwórz konstruktor (__init__) dla klasy "Człowiek", który oprócz imienia pobierze też wzrost i wagę.
# tylko konstruktor wrzucić na stronę


class Czlowiek:
    def __init__(self, imie, wzrost, waga):
        self.imie = imie
        self.wzrost = wzrost
        self.waga = waga


    def speak(self):
        print('Mówię prawdę.')

    def count_bmi(self):
        pass

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


anna = Czlowiek('Anna', 165, 55)
adam = Czlowiek('Adam', 185, 90)

print(adam.waga)
print(adam.wzrost)

print(anna.waga)
print(anna.wzrost)

