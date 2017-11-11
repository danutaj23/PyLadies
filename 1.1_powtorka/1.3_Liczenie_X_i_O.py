# Napisz funkcję, która sprawdzi, czy liczba znaków "x" i "o" w stringu
# jest taka sama i zwróci True/False.
# Jeśli string zawiera coś innego niż "x" lub "o", to wypisze błąd.
# >>> xo_checker("xoxoxoxoxoxo") True
# >>> xo_checker("xxxoooxxxxxxxo") False
# >>> xo_checker("xpd") "Illegal letters in text"


def xo_checker(string):
    x = 0
    o = 0
    for letter in string:
        if letter in "x":
            x += 1
        elif letter in "o":
            o += 1
        else:
            return "Illegal letters in text"
    if x == o:
        return True
    else:
        return False


print(xo_checker("xoxoxoxoxoxo"))
print(xo_checker("xxxoooxxxxxxxo"))
print(xo_checker("xpd"))
