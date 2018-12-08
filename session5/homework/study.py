def count_letter_freq(inputStr):
    letter = {
 
    }
    for i in inputStr:
        letter[i] = inputStr.count(i)
    for j in sorted(letter):
        if j != ' ':
            print(j + ' ' + str(letter[j]))
Inputstring = input("input a string: ")
Inputstring = Inputstring.lower()            
count_letter_freq(Inputstring)
