import pyrebase
import firebase_config

firebase_config = firebase_config.Firebase().firebase_config
firebase = pyrebase.initialize_app(firebase_config)

db = firebase.database()

## POST method
def create():
    data = {
        "name": "Tom",
        "age": 29,
        "address": {
            "street_name": "av. street",
            "number": 1000,
            "postal_code": "50000-500",
        },
    }

    db.child("address").push(data=data)
    ## specifying ID of document
    ### db.child("address").child(data.name).set(data)


## create()


def update():
    ## updating with document ID
    ## db.child("addreess").update({"age": 35})
    ## data = {
    # "address/<ID>": {"age": 35},
    # "address/<ID>/address": {"number": 1001},
    # }
    name = "Tom"
    address_list = db.child("address").get()
    for address in address_list.each():
        # print(address.val())
        # print(address.key())
        if address.val()["name"] == name:
            key = address.key()

        db.child("address").child(key).update({"age": 35})
    # db.update(data)


## update()


def delete():
    item_or_document_to_delete = "Jane"
    all_documents = db.child("address").get()
    for document in all_documents.each():
        if document.val()["name"] == item_or_document_to_delete:
            key = document.key()

            db.child("address").child(key).remove()


## delete()
