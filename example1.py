import requests
import sys
import urllib.parse
import json

#χρησιμοποίησα την έκδοση της python 3.6.2
main_Api="https://api.teleport.org/api/urban_areas/"
list_scores_of_first_city = []
list_scores_of_second_city = []
scoresA=0
scoresA=0

print("Δώσε την πρώτη πόλη")
city_first = sys.stdin.readline()
print("Δώσε την δεύτερη πόλη")
city_second = sys.stdin.readline()


url1 =main_Api+"slug:"+slug+"/scores/"
url2 =main_Api + urllib.parse.urlencode({'slug': city_second }) +"/scores/"

json_data1 = requests.get(url1).json()
json_data2 = requests.get(url2).json()


for i in range (0,13):
  list_scores_of_first_city.append(json_data1['categories'][i]['score_out_of_10'])
  list_scores_of_second_city.append(json_data2['categories'][i]['score_out_of_10'])
#δοκιμή
#print ( list_scores_of_first_city)
#print ( list_scores_of_second_city)

for i in range (0,13):
    if list_scores_of_first_city[i]>list_scores_of_second_city[i]:
         scoresA=+1
    else :
         scoresB=+1


print("Η πρώτη πόλη υπερέχει της δεύτερης σε"+ scoresA + " από τους 14 .Ενώ αντίστοιχα η ΔΕΥΤΕΡΗ ΠΟΛΗ σε "+ scoresB + " από τους 14")

