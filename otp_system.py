import random
import requests

API_KEY = "qJpaR8xtl4XKZN2fGbFcIgwjod97himOLQ0UrDEVAu1nWkvyC3s9gmI7KBvTqMFoUNjl8Of4AEwap6rG"

def generate_otp():

    otp = random.randint(1000,9999)

    url = "https://www.fast2sms.com/dev/bulkV2"

    payload = {
        "authorization": API_KEY,
        "route": "v3",
        "message": f"Your OTP is {otp}",
        "language": "english",
        "numbers": "9523317482"
        
    }

    headers = {
        "cache-control": "no-cache"
    }

    response = requests.get(url, headers=headers, params=payload)

    print("OTP Sent:", otp)

    return otp