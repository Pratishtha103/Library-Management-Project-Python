from ReturnBook import *
import razorpay
keyid='rzp_test_2ygIkm41kBnPQJ'
keysecret='K0HdVQEH8mKamdNWRbIqVvvj'
client = razorpay.Client(auth=(keyid, keysecret))
# pay_this_fine=fine.get()
# f=int(pay_this_fine)
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