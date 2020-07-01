import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import requests

cred = credentials.Certificate("firebasecreds.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://phone2word.firebaseio.com/"
})

ref = db.reference('/mappings')
f = open("final_wordlist.txt", "r")
lst = f.readlines()
for i in range(100000):
    numberword = ""
    if i < 10:
        numberword = "0000" + str(i)
    elif i < 100:
        numberword = "000" + str(i)
    elif i < 1000:
        numberword = "00" + str(i)
    elif i < 10000:
        numberword = "0" + str(i)
    key = ref.push({
        'word': lst[i].rstrip("\n"),
        'number': numberword
    })
    print(key)