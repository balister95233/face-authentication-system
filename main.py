from face_auth import detect_face
from otp_system import generate_otp

print("Starting Authentication System")

face = detect_face()

if face:
    print("Face detected")

    otp = generate_otp()

    user_otp = input("Enter the OTP: ")

    if user_otp == str(otp):
        print("Access Granted")
    else:
        print("Wrong OTP - Access Denied")

else:
    print("Face not detected")