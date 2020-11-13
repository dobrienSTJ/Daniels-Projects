from firebase import firebase
firebase = firebase.FirebaseApplication('https://cookietest-a4f79.firebaseio.com', None)

#READING DATA

#reads the database at the node /dht
result = firebase.get('/dht', None)
print(result)

#you can also read along the tree further down /dht/humidity 
result = firebase.get('/dht/humidity', None)
print(result)
