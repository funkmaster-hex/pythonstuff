#!/usr/bin/env python3
import math

def getfilename():
    file = input("Enter the absolute path to your file: ")
    return file

def getcodetype():
    print ("Enter the algorithm you wish to use: ")
    print ("1)Base2 ")
    print ("2)Base16 ")
    print ("3)Base32 ")
    print ("4)Base64 ")
    codechoice = int(input(": "))

def encodedecode(encode, decode):
    listylist = {'0': 0,
                 '1': 1,
                 '2': 2,
                 '3': 3,
                 '4': 4,
                 '5': 5,
                 '6': 6,
                 '7': 7,
                 '8': 8,
                 '9': 9,
                 'A': 10,
                 'B': 11,
                 'C': 12,
                 'D': 13,
                 'E': 14,
                 'F': 15,
                 'G': 16,
                 'H': 17,
                 'I': 18,
                 'J': 19,
                 'K': 20,
                 'L': 21,
                 'M': 22,
                 'N': 23,
                 'O': 24,
                 'P': 25,
                 'Q': 26,
                 'R': 27,
                 'S': 28,
                 'T': 29,
                 'U': 30,
                 'V': 31,
                 'W': 32,
                 'X': 33,
                 'Y': 34,
                 'Z': 35,
                 'a': 36,
                 'b': 37,
                 'c': 38,
                 'd': 39,
                 'e': 40,
                 'f': 41,
                 'g': 42,
                 'h': 43,
                 'i': 44,
                 'j': 45,
                 'k': 46,
                 'l': 47,
                 'm': 48,
                 'n': 49,
                 'o': 50,
                 'p': 51,
                 'q': 52,
                 'r': 53,
                 's': 54,
                 't': 55,
                 'u': 56,
                 'v': 57,
                 'w': 58,
                 'x': 59,
                 'y': 60,
                 'z': 61,
                 '!': 62,
                 '"': 63,
                 '#': 64,
                 '$': 65,
                 '%': 66,
                 '&': 67,
                 "'": 68,
                 '(': 69,
                 ')': 70,
                 '*': 71,
                 '+': 72,
                 ',': 73,
                 '-': 74,
                 '.': 75,
                 '/': 76,
                 ':': 77,
                 ';': 78,
                 '<': 79,
                 '=': 80,
                 '>': 81,
                 '?': 82,
                 '@': 83,
                 '[': 84,
                 '\\': 85,
                 ']': 86,
                 '^': 87,
                 '_': 88,
                 '`': 89,
                 '{': 90,
                 '|': 91,
                 '}': 92,
                 '~': 93}
    if encode:
        numtoconvert = getfile()
        base = 2
        convertvar = int(input("Please enter the base that you would like to convert to: "))
    elif decode:
        numtoconvert = getfile()
        base = int(input("Please enter the base that your file is in: "))
        convertvar = 2

    integer = 0
    for character in numtoconvert:
        assert character in listylist, 'Invalid character. Moron.'
        value = listylist[character]
        assert value < base, 'Number outside base. Idiot.'
        integer *= base
        integer += value

    reverseit = dict(map(reversed, listylist.items()))

    array = []
    while integer:
        integer, value = divmod(integer, convertvar)
        array.append(reverseit[value])
    answer = ''.join(reversed(array))

    print (answer)
        
def main():
    mainmenu = True
    encode = False
    decode = False
    while mainmenu:
        print ("Choose an operation:")
        print ("1)Encode a file")
        print ("2)Decode a file")
        print ("3)Quit")
        firstchoice = int(input(": "))
        if firstchoice == 1:
            encode = True
            encodedecode(encode, decode)
        elif firstchoice == 2:
            decode = True
            encodedecode(encode, decode)
        elif firstchoice == 3:
            mainmenu = False
        else:
            print ("Invalid Decision... Moron.")




if __name__ == '__main__':
    main()


'''References: Potential code from each source, made to fit my POS Program.  
http://code.activestate.com/recipes/65212/
http://stackoverflow.com/questions/23020520/how-to-convert-binary-to-decimal-using-python-without-using-the-bin-function
http://www.cs.trincoll.edu/~ram/cpsc110/inclass/conversions.html
https://www.quora.com/How-do-I-write-a-program-in-Python-that-can-convert-an-integer-from-one-base-to-another
https://docs.python.org/3/library/base64.html
http://stackoverflow.com/questions/3973685/python-homework-converting-any-base-to-any-base''' 
