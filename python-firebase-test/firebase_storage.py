import pyrebase
import firebase_config
import urllib

firebase_config = firebase_config.Firebase().firebase_config
firebase = pyrebase.initialize_app(firebase_config)

## setting up storage
storage = firebase.storage()

## upload file to storage
file_name = input("Enter the name of the file you want to upload:\n")
cloud_file_name = input("Enter the name of the file in storage:\n")
storage.child(cloud_file_name).put(file_name)

## getting URL of file uploaded
print(storage.child(cloud_file_name).get_url(None))

## download link
## download_link = input("Enter download URL:\n")
### /notes/peace.txt
## storage.child(download_link).download("", "peace.png")

## reading from a file in storage
path = input("Enter the path, in storage, of the file you want to read:\n")
print(storage.child(path).get_url(None))
url = storage.child(path).get_url(None)
file_read = urllib.request.urlopen(url).read()
print(file_read)
