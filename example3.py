import sys
import urllib.parse
import requests

print("north=44.1,south=-9.9,east=-22.4,west=55.2 ")
#αυτό είναι το κύριο api στο οποίο θα προσθέσουμε τα ορίσματα
main_api = 'http://api.geonames.org/citiesJSON?'
#εδώ ο χρήστης θα εισάγει τέσσερα σημεία
print("Δώσε τον βορρά")
north = sys.stdin.readline()
print("Δώσε τον νότο")
south = sys.stdin.readline()
print("Δώσε την ανατολή")
east = sys.stdin.readline()
print("Δώσε την Δύση")
west = sys.stdin.readline()
#εδώ θα προσθέσω τα ορίσματα στο api και συγκεκριμένα είναι:north ,south ,east,west
#orderby=population για να μου δώσει τα αποτελέσματα των πόλεων με τον μεγαλύτερο ως τον μικρότερο πληθυσμό
#lang=en για την γλώσσα που θέλουμε να μας επιστραφεί το αποτέλεσμα
#και username με το ψευδώνυμο που έχω κάνει τον λογαριασμό

url = main_api + urllib.parse.urlencode({'north': north})
url = url+ "&" + urllib.parse.urlencode({'south':south})
url = url+ "&" + urllib.parse.urlencode({'east':east})
url = url+ "&" + urllib.parse.urlencode({'west':west})
orderby="population"
url = url+ "&" + "orderby=" +orderby
lang = "en"
url = url +"&"+ urllib.parse.urlencode({'lang':lang})
username = "MasterDisaster"
url = url+ "&" + "username=" +username

json_data = requests.get(url).json()
#από το αποτέλεσμα που είναι σε μορφή json θα επιστραφεί στον χρήστη μόνο το όνομα της πόλης με τον μεγαλύτερο πληθυσμό
print(json_data['geonames'][0]['name'])