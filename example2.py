import requests


#χρησιμοποίησα την έκδοση της python 3.6.2

url="https://api.chucknorris.io/jokes/random"
json_data = requests.get(url).json()
#Εμφάνιση τυχαίας φράσης
print (json_data['value'])

phrase=json_data['value']
#εδώ βάζω την φράση σε μια λίστα για να την χωρίσω σε λέξεις
list_phrase = phrase.split(" ")

for i in range(0, len(list_phrase) - 1):

    if (len(list_phrase[i]) > 1):  # Αν το μέγεθος της λέξης είναι μεγαλύτερο από 1. Απο 2 και πάνω
        temp = list_phrase[i]
        number = ord(temp[:1]) + ord(
            temp[len(temp) - 1:])  # προσθέτω τους δύο ακριανούς χαρακτήρες θεωρώντας τους τύπου ASCII
        final = number % 3  # Καταχωρω το υπόλοιπο του παραπάνω αθροίσματος με το 3
    else:  # Αλλιώς επιστρέψω το -1 αν η λέξη έχει 1 χαρακτήρα
        final = -1



        print(final, " ", end='')  # Για να εκτυπώνονται στην ιδια γραμμή σαν αριθμιτική παράσταση


