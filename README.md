<img
  src="Images/logo2.jfif"
  alt="Logo"
  title="HackaThon"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
# Hackathon AllHacks4Good
<img
  src="Images/logo.jfif"
  alt="Logo"
  title="Logo"
  style="display: inline-block; margin: 0 auto; max-width: 300px">
## Forgetful Beacon
---

Forgetful Beacon helps locate people with dissociative amnesia, while safeguarding personal information. Facial recognition is used to identify a person and send an alert to their emergency contact.

### Objective

The objective is to help people with dissociative amnesia to be reunited with their family/caregivers if they get lost during a dissociative episode, while safeguarding their personal data from strangers. To do this, the program uses facial recognition to identify the user and sends an alert to their emergency contact(s), who will receive the picture, to corroborate the identity of the lost person, and the location of where they were found.

### How we built it

The main idea was to develop an app that could identify a lost person given a database with their facial characteristics, name, location, contacts, age and health problems. A samaritan would take a photo to a QR code paste on the lost person that is linked to our app and will require to take a facial's photo that will send it to a given server with an facial recognition algorithm linked to the database and alert to the relative partners of the lost person.

The web app could be seen at the following link: [ForgetfulBeacon](https://www.forgetfulbeacon.tech/). This web app asks for new users their personal information such as name, contacts, location, email and parent, then these users have to register their relative partners that want to be registered on the database (All these users were named as principal users), from now on, each time that could be lost their relative partners will receive an alert of their information and last location.

The database was made at cockroachlabs with a principal table (for the lost relative partners), secondary table (for the users registered), contact table (with the differents kind of contact that could be made for the users) and disability table (with medical diagnostics from the lost people)

To insert the registers we made use of `connect.py` that connect to the cockroach data base, convert the images to and array of bytes and send all the information to the database. The idea here was to connect the web app to this cockroach data base and benefit from the architecture that cockroach could give such as speed, availability and high scalability.

In order to make the facial recognition algorithm, we made use of OpenCV's functions such as videoCapture and CascadeClassifier (as first approach given the time that we have left). Those that are named as `faceDetection.py`,`faceEyeDetection.py`, `faceSmileDetection.py`, `faceSmileEyeDetection.py` were used as calibration files for the given facials photos. `01_face_dataset.py` make a video of 20 images from the person that will give a yaml file with and make a label for the classification algorithm. `02_face_training.py` will train the images uploaded from the database, and finally `03_face_recognition.py` will classify the new photo that a samaritan will post to our web app.

### Challenges we ran into

1. Technical details such as the connection to our local computer to the cockroach data base with Python, this was due to the Python version, although we could solve the problem we needed to downgrade our Python version to 3.8.
2. Integration with OpenCV with dlib due to lack of lib tools from C, we could solve this problem by updates from Manjaro's packages.
3. Integration of the cockroach data base to the web app made on Wix, this problem couldn't be solved because we needed to pay for this specifi integration.
4. Connection from the web app widgets to the local collector that Wix give us, this problem couldnt be solved due to lack of time.

### Accomplishments that we're proud of

* Team colaboration
* Make use of new tools without knowing them
* Project template that could our community


