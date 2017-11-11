# Wykorzystując dwie nowe wbudowane char() ord() >>> ord("a") 97 >>> chr(98) "b" funkcje
# zaimplementuj szyfr cezara, który jako drugi parametr będzie brał przesunięcie.
# Przykłady:
# szyfr cezara o parametrze 3 podmieni każdą literka alfabetu na trzecią z kolei np A na D a Z na C.
# >>> cezar("abc", 2) "cde"
# >>> cezar("abc", -2) "yza"
# Pamiętaj żeby znaki inne niż litery nie zmieniać. Uwzględnij dodatkowo wielkie litery.


def cezar(tekst, przesuniecie):
    zaszyfrowany_tekst = ""
    for letter in tekst:
        numer = ord(letter)
        numer += przesuniecie
        if letter.isalpha():
            if letter.islower():
                if numer > ord("z"):
                    numer -= 26
                elif numer < ord("a"):
                    numer += 26
            else:
                if numer > ord("Z"):
                    numer -= 26
                elif numer < ord("A"):
                    numer += 26
            zaszyfrowany_tekst += chr(numer)
        elif letter.isalnum():
            zaszyfrowany_tekst += letter
        elif letter in " ":
            zaszyfrowany_tekst += " "
    return zaszyfrowany_tekst


print(cezar("abc", 2))
print(cezar("abc", -2))
