# Zapisz średni wzrost postaci dla każdego z kolorów w osobnych linijkach w formie:
# Średni wzrost osób z kolorem oczu blue wynosi 123,12 cm.

file = open('py1.2.txt', 'r')

dictionary = {}

for data in file:
    name = data[data.find(".") + 2:data.find(" has")]
    eyes = data[data.find("has") + 4:]
    eyes = eyes[:eyes.find(" and")]
    height = int(data[data.find(" is ") + 3:data.find(" cm")])
    dictionary[name] = {"Eyes: ": eyes, "Height: ": height}

file.close()

eye_dictionary = {}
for name in dictionary:
    eye_color = dictionary[name]["Eyes: "]
    height = dictionary[name]["Height: "]
    if eye_color in eye_dictionary:
        eye_dictionary[eye_color].append(height)
    else:
        eye_dictionary[eye_color] = [height]

for eye_color in eye_dictionary:
    avg = sum(eye_dictionary[eye_color]) / len(eye_dictionary[eye_color])
    print("Średni wzrost osób z kolorem oczu {} wynosi {}".format(eye_color, avg))

#co z dwukolorowymi oczami?