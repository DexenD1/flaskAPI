import requests, json

url = 'http://YOUR_INSTANCE_EXTERNAL_IP/analyze' # Ex: 'http://127.0.0.1/analyze'
uri = "gs://YOUR_BUCKET_NAME/" # Ex: "gs://an-example.appspot.com/"
fileName = "AN_IMAGE_STORED_IN_STORAGE_BUCKET_ALONG_WITH_EXTENTION" # Ex: "cumulonimbus.jpg"
result = requests.post(url+"?uri="+uri+"&fileName="+fileName)

# convert server response into JSON format.
print(result.text)