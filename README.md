# flaskAPI
 Bangkit 2021 Final Project (Flask API)
# Descriptions
 This source code is meant to analyze an image (using AutoML Vision) stored in Google Cloud Storage through an APIs service made from Flask. This service will run on a Docker container.
# Instructions
 1. Clone this repository.
 2. Create service account for a Compute Instance:
     1. Spawn a Google Cloud Shell
     2. _gcloud iam service-accounts create **flask-api**_
     3. _gcloud projects add-iam-policy-binding **YOUR_PROJECT_ID** --member="serviceAccount:**flask-api**@**YOUR_PROJECT_ID**.iam.gserviceaccount.com" --role="roles/owner"_
        It is recommended to use best practice of least privelege.
     4. _gcloud iam service-accounts keys create **key.json** --iam-account=**flask-api**@**YOUR_PROJECT_ID**.iam.gserviceaccount.com_
     5. Copy the created _**key.json**_ into previously created Compute Engine
     6. Export an environment variable in the Compute Engine:
        _export GOOGLE_APPLICATION_CREDENTIALS="**KEY_PATH**"_
 3. Build a Docker image (you should have Docker installed in your Compute Instance: https://docs.docker.com/engine/install/ubuntu/):
     1. _cd flaskAPI_
     2. _sudo docker build -t flask-api-image ._
     3. _sudo docker run -p 80:5000 --name flask-api -d flask-api-image_
     4. _sudo docker ps_
 4. Test the API:
     1. Edit and configure variable values in this script:
        _python3 test.py_
     2. Output example:
         *{
           "message": {
             "imageName": "cumulonimbus.jpg",
             "labels": [
               "Cloud",
               "Sky",
               "Atmosphere",
               "Cumulus",
               "Landscape",
               "Horizon",
               "Geological phenomenon",
               "Calm",
               "Electric blue",
               "Meteorological phenomenon"
             ]
           },
           "status": "UP"
         }*
 5. Done.
