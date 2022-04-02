import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import streamlit as st

st.title('WalkMan')
st.header('Digital-Address')

if not firebase_admin._apps:
    cred_obj = firebase_admin.credentials.Certificate("acckey.json")
    default_app = firebase_admin.initialize_app(cred_obj, {
	    'databaseURL':"https://walkman-hq-default-rtdb.firebaseio.com/"
	})

db=firestore.client()


try:
    data={'Address':['Brookfields', 'VR Mall','Rajalakshmi college','KGiSL'],
    'DAC Code':['ACBD33162254','GHFH00302622','UOPI88976863','OYPT88123647'],
    'Location':['https://www.google.com/maps/place/Brookefields/@11.0088682,76.9573476,17z/data=!3m1!4b1!4m5!3m4!1s0x3ba859015dcbbe93:0x48ced40a587ca58e!8m2!3d11.0088682!4d76.9595363', 'https://www.google.com/maps/place/VR+Mall/@13.0812013,80.1944245,17z/data=!3m1!4b1!4m5!3m4!1s0x3a5265d2cee4cea7:0xc4ec502d88716ff!8m2!3d13.0812013!4d80.1966132', 'https://www.google.com/maps/place/Rajalakshmi+Engineering+College/@13.0085334,80.0012808,17z/data=!3m1!4b1!4m5!3m4!1s0x3a528c9ebac84723:0x18e2bf88dfefa3ed!8m2!3d13.0085334!4d80.0034695', 'https://www.google.com/maps/place/KGiSL+Institute+of+Technology/@11.0847815,76.9958342,17z/data=!3m1!4b1!4m5!3m4!1s0x3ba8f792636f82b5:0xdc86449e9fb48675!8m2!3d11.0847815!4d76.9980229'],
    }
    db.collection('dac').add(data)
    a=st.text_input("You Are Entering Address or DAC Code:")
    b=st.text_area("Enter the value from the key:")
    button=st.button("Search")
    c=data[a]
    e=c.index(b)
    for i in data:
        if i==a:
            print('\n',data[a][e],end=' ')
        else:
            print('\n',data[i][e],end=' ')
except(KeyError):
    print("Invalid address")

