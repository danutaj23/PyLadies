from pprint import pprint as pp

# pół choinki z liter
# i = 1
# for letter in "ala ma kota":
#     print(letter * i)
#     i += 1

zliczacz={}
wyraz = input('podaj wyraz: \n')
for letter in wyraz:
    if letter in zliczacz:
        zliczacz[letter] += 1
    else:
        zliczacz[letter] = 1
    print(zliczacz)
pp(zliczacz)
