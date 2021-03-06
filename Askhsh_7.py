#Εκφώνηση
#Γράψτε ένα πρόγραμμα σε Python το οποίο δεδομένης της τρέχουσας μέρας (πχ Δευτέρα 8/1/2018) υπολογίζει πόσες Δευτέρες θα υπάρξουν τα επόμενα 10 χρόνια
# που θα είναι η όγδοες του εκάστοτε μήνα.

######################################################################################################################################################################
from datetime import date, timedelta
import datetime

#Στην συνάρτηση αυτή παίρνω τον χρόνο που δόθηκε ως όρισμα και επιστρέφει την ημερομηνία που τηρεί της προυποθέσεις αφού ελέγξει και για
#τους 12 μήνες του ίδιου χρόνου
#οι προυποθέσεις είναι ο αριθμός - ημέρα της ημερομηνίας του χρόνου να είναι ίδια με αυτή στο όρισμα ΚΑΙ ο ακέραιος που αντιστοιχεί στο όνομα-ημέρα της ημερομηνίας του χρόνου να είναι ίδιος με αυτή στο όρισμα

def currentday(year,day,daynum):
    n = datetime.date.today()
    if(year > n.year):
        n = date(year,1,day)
    while n.month < 12:
        if (n.weekday() == daynum):
            yield n
        n = date(n.year,n.month+1,day)
    if (n.weekday() == daynum):
        yield n

#Ημερομηνία του συστήματος
today = datetime.date.today()

#Η συνάρτηση currentday θα κληθεί 10 φορές (όσα και τα χρόνια που έχουν ζητηθεί στην εκφώνηση)
#περνά ως όρισμα τρεις μεταβλητές
#τον χρόνο που έχουμε σήμερα προθέτοντας κάθε φορά την μεταβλητή i που αναπαριστα τα χρόνια
#το αριθμό της τρέχουσα ημερομηνίας -ημέρα
#την ημέρα που αντιστοιχεί στην τρέχουσα ημερομηνία πχ Δευτέρα 0 ,Τρίτη 1, Τετάρτη 2 ,Πεμπτη 3 και ούτω κάθεξης.

for i in range(11):
    for d in currentday(today.year+i,today.day,today.weekday()):
       print(d)
