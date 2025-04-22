from quotexapi.stable_api import Quotex

q = Quotex(email="truptiauti2001@gmail.com", password="Samarth@123")

if q.connect():
    print("✅ Login Successful")
else:
    print("❌ Login Failed")
