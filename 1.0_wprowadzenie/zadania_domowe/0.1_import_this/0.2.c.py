# Wypisanie jednego słowa znadującego się przed słowem 'is'.

zen = "Beautiful is better than ugly. \n" \
      "Explicit is better than implicit. \n" \
      "Simple is better than complex. \n" \
      "Complex is better than complicated. \n" \
      "Flat is better than nested. \n" \
      "Sparse is better than dense. \n" \
      "Readability counts. \n" \
      "Special cases aren't special enough to break the rules. \n" \
      "Although practicality beats purity. \n" \
      "Errors should never pass silently. \n" \
      "Unless explicitly silenced. \n" \
      "In the face of ambiguity, refuse the temptation to guess. \n" \
      "There should be one-- and preferably only one --obvious way to do it. \n" \
      "Although that way may not be obvious at first unless you're Dutch. \n" \
      "Now is better than never. \n" \
      "Although never is often better than *right* now. \n" \
      "If the implementation is hard to explain, it's a bad idea. \n" \
      "If the implementation is easy to explain, it may be a good idea. \n" \
      "Namespaces are one honking great idea -- let's do more of those!' \n"

for zdanie in zen.split('\n'):
    if ' is ' in zdanie:
        slowo_przed_is = zdanie[:zdanie.find(' is ')]
        if slowo_przed_is.count(' ') >= 1:
            slowo_przed_is = slowo_przed_is[slowo_przed_is.rfind(' '):]
        if slowo_przed_is:
            print(slowo_przed_is)
    else:
        pass
