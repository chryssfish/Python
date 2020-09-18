######################################################################################################################################################################
import string
import random

string.letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
matrix = [[random.choice(string.letters) for i in range(100)] for j in range(100)]

userfile=str(input("Give your text file . \n"))
f = open(userfile, 'r')

key = 0

for line in f:
    word=list(line)
    wordlen = len(word)-1

    for i in range (100):
        for j in range (100):
            #prvto grAMMA
            if word[0] in matrix[i][j]:
                for z in range(wordlen):
                    w = j + z
                    if w < 100:
                        #to gramma
                        if word[z] in matrix[i][j+z]:
                            key += 1
                if key == wordlen:
                    print("The word", line , "was found horizontically")
                key = 0
                for z in range(wordlen):
                    w = i + z
                    if w < 100:
                        if word[z] in matrix[i+z][j]:
                            key += 1
                if key == wordlen:
                    print("The word ", line , "was found vertically")
                key = 0
