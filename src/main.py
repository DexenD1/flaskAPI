# Import standart libraries
from flask import Flask, jsonify, request
from google.cloud import vision, firestore

# Initialize Flask Application
app = Flask(__name__)

# API that returns JSON as a result after processing an image
@app.route("/analyze", methods=["GET", "POST"])
def analyze():
    # Creates an AutoVision client
    visionClient = vision.ImageAnnotatorClient()

    # Receive the uri and image name from url
    uri = request.values.get("uri")
    fileName = request.values.get("fileName")

    # Analyze the image from bucket with AutoVision
    labels = []
    result = visionClient.label_detection(image=vision.Image(source=vision.ImageSource(image_uri=uri+fileName)))
    for label in result.label_annotations:
        labels.append(label.description)

    return jsonify({
        "status": "UP",
        "message": {
            "imageName": fileName,
            "labels": labels
        }
    }), 200

# API that returns a list of the image along with information about the image from Firestore
@app.route("/databasequery", methods=["GET"])
def databaseQuery():
    # Creates a Firestore client
    firestoreClient = firestore.Client()
    # Create a reference from the 'images' collection
    collectionRef = firestoreClient.collection(u"images")

    # Query all the document listed in the 'images' collection
    queryResult = []
    for doc in collectionRef.stream():
        information = []
        for field, info in doc.to_dict().items():
            information.append({field: info})

        queryResult.append(
            {
                "docId": doc.id,
                "information": information
            }
        )

    return jsonify({
        "status": "UP",
        "message": queryResult
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")