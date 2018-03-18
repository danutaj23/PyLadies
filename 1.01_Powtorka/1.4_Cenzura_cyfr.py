# Napisz funkcję, która zamieni wszystkie cyfry na "#" w tekście (stringu)
# >>> cenzura_cyfr("password12345") "password#####"
# >>> cenzura_cyfr("a1a ma k0ta") "a#a ma k#ta"

def cenzura_cyfr(zdanie):
    ocenzurowane_zdanie = ""
    for znak in zdanie:
        cyfry = "0123456789"
        if znak in cyfry:
            ocenzurowane_zdanie += "#"
        else:
            ocenzurowane_zdanie += znak
    return ocenzurowane_zdanie


print(cenzura_cyfr("password12345"))
print(cenzura_cyfr("a1a ma k0ta"))

