from ReturnBook import *
import razorpay
keyid='Your key id'
keysecret='Your key secret'
client = razorpay.Client(auth=(keyid, keysecret))
#checkout
data = { 
    "amount": 1*100, 
    "currency": "INR", 
    "receipt": "LibraryManagement",
    "notes": {
        "name" :"XYZ College",
        "Payment_for": "Library"

    }
    }
#server order id
order = client.order.create(data=data)
print(order)
