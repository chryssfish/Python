#Εκφώνηση
#Γράψτε ένα πρόγραμμα σε Python το οποίο παράγει ένα τετράγωνο 100*100 το οποίο αποτελείτε από τυχαίους κεφαλαίους λατινικούς χαρακτήρες.
# Στην συνέχεια χρησιμοποιήστε σαν λεξικό ένα αρχείο το οποίο θα σας δώσει ο χρήστης (μία λέξη ανά γραμμή) ώστε να επιστρέψετε τις λέξεις του λεξικού που περιέχονται
# οριζόντια ή κάθετα στο τετράγωνο που φτιάξατε.

######################################################################################################################################################################
import string
import random

#Δημιουργία τετραγώνου 100*100 με τυχαία κεφαλαία γράμματα
string.letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
matrix = [[random.choice(string.letters) for i in range(100)] for j in range(100)]

#Ο χρήστης δίνει το αρχείο που έχει γράψει τις λέξεις
userfile=str(input("Give your text file . \n"))
f = open(userfile, 'r')

key = 0

#Για κάθε λέξη στο αρχείο
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
