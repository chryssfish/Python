#Εκφώνηση
#Γράψτε ένα πρόγραμμα σε Python το οποίο παίρνει σαν είσοδο από το χρήστη έναν ακέραιο και τον μετατρέπει σε λατινική μορφή (Οι αριθμοί είναι μέχρι 1000000).

#Συνάρτηση Μετατροπής Ακέραιου σε Λατινική Μορφή
def convert_to_Roman(num):
   val = (1000000,500000,100000,50000,10000,5000,1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
   syb = ('M̄','D̄','C̄','Ḹ','X̄','V̄','Ī',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
   roman_num = ""
   for i in range(len(val)):
      count = int(num / val[i])
      roman_num += syb[i] * count
      num -= val[i] * count
   return roman_num

num=int(input("Give an integer from 1 to 1000000 \n"))
print("The number you gave has been converted to latin form : ",convert_to_Roman(num))
