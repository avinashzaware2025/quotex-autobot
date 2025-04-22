from quotexapi.stable_api import Quotex
import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("QX_EMAIL")
password = os.getenv("QX_PASSWORD")

q = Quotex(email=email, password=password)

if q.connect():
    print("✅ Login Successful")
else:
    print("❌ Login Failed")
