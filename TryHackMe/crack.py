#!/usr/bin/env python3

import math
#chosenPass = ''' !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~'''   #### This was used to find the "hash" for each character
print('[1] "Hash" a password.\n[2] "Crack" a hash.')
option = input("Please enter which function you would like to perform: ")

# "Hashing" a pass
def int_array_to_text(int_array):
    txt = ''
    for i in range(len(int_array)):
        txt += ''.join(chr(97+int_array[i]))
    return txt

def string_to_int_array(string):
    global intArr
    intArr = []
    for i in range(len(str(string))):
        charcode = ord(string[i])
        partA = math.floor(charcode / 26)
        partB = charcode % 26       
        intArr.append(partA)
        intArr.append(partB)
    return intArr

if(option == "1"):
    chosenPass = input('Please enter a password to hash: ')
    hashtest = int_array_to_text(string_to_int_array(int_array_to_text(string_to_int_array(chosenPass))))
    print(hashtest)

# "Cracking" the hash
letters = "dudzdueaduebduecdueddueeduefduegduehdueiduejduekduelduemduendueoduepdueqduerduesdvdtdvdudvdvdvdwdvdxdvdydvdzdveadvebdvecdveddveedvefdvegdvehdveidvejdvekdveldvemdvendveodvepdveqdverdvesdwdtdwdudwdvdwdwdwdxdwdydwdzdweadwebdwecdweddweedwefdwegdwehdweidwejdwekdweldwemdwendweodwepdweqdwerdwesdxdtdxdudxdvdxdwdxdxdxdydxdzdxeadxebdxecdxeddxeedxefdxegdxehdxeidxejdxekdxeldxemdxendxeodxep"
if(option == "2"):
    hashed = input("Please enter a hash: ")
    n = 4 # Splits letters and hashed into groups of four
    letters = [(letters[i:i+n]) for i in range(0, len(letters), n)]
    hashed = [(hashed[i:i+n]) for i in range(0, len(hashed), n)]

    def match_test():
        for i in range(len(hashed)):
            for letter in letters:
                if(letter == hashed[i]):
                    print(chr(letters.index(letter)+32),end = "")
    match_test()
