import sys
import random
import os

#ΤΟ ΠΡΟΓΡΑΜΜΑ ΕΓΙΝΕ ΜΕ ΣΕΙΡΙΑΚΗ ΑΝΑΖΗΤΗΣΗ ΨΑΧΝΟΝΤΑΣ ΓΡΑΜΜΑ ΓΡΑΜΜΑ

maxLetter = 0                                              #Η μεταβλητή που κρατά τον αριθμό των γραμμάτων της μεγαλύτερης λέξης
y = 0
max_i = 0                                                  #Η θέση του τελευταίου γράμματος της μεγαλύτερης λέξης
print("Εισάγετε πρόταση")
Phrase = sys.stdin.readline()                              #Διαβάζω την πρόταση
for i in range (1, len(Phrase) + 1):                       #από την αρχή + 1 μέχρι το τέλος της πρότασης + 1
    if (Phrase[i-1:i] != " ") and (i != len(Phrase)):      #Προσθέτω πόσα γράμματα έχει η λέξη μέχρι να συναντήσω το κενό χαρακτήρα
        y += 1                                             #Η δεύτερη συνθήκη είναι γιατί στο τέλος της πρότασης δέν θα έχω κενό, οπότε αν είναι τελευταία η μεγαλύερη λέξη πρέπει να την πάρω
    else:
        if (y >= maxLetter):                               #Βρίσκω την μεγαλύτερη λέξη και κρατάω τα στοιχεία της
            maxLetter = y                                  #Σε περίτωση ισοψηφίας πέρνω την πιο πρόσφατη λέξη με την συνθήκη (y >= maxLetter)
            max_i = i
        y = 0                                              #Επαναφέρω τον μετρητή γραμμάτων

print (Phrase[max_i - maxLetter - 1 : max_i - 1 ])

