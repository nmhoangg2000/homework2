def count_letter_freq(inputStr):
    letter = {
        "a": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "l": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "w": 0,
    }
    for i in inputStr:
        letter[i] = inputStr.count(i)
    for j in sorted(letter):
        if j != ' ':
            print(j + ' ' + str(letter[j]))
Inputstring = input("input a string: ")
Inputstring = Inputstring.lower()            
count_letter_freq(Inputstring)
