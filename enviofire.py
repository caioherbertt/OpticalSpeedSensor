import random
import pyrebase
random.seed(2)

config = {
  "apiKey": "AIzaSyAW4RY8ttu7Sqyv2ZfpPD6NoTn1s1Cd2h4",
  "authDomain": "opticalspeedsensor.firebaseapp.com",
  "databaseURL": "https://opticalspeedsensor-default-rtdb.firebaseio.com/",
  "storageBucket": "opticalspeedsensor.appspot.com"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()
dado1 = "432432"
dado = random.random()
db.child("Sensor2").child("Medida").push(dado1)
