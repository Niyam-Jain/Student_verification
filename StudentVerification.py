import cv2
from pyzbar import pyzbar
from PIL import Image
import json


Data_file = "student_database.json"

def load_database():
    try:
        with open(Data_file, "r") as file:
            Data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        Data = {}
    return Data

def read_qr_code(image_path):
    image = cv2.imread(image_path)
    qr_codes = pyzbar.decode(image)
    for qr_code in qr_codes:
        qr_data = qr_code.data.decode("utf-8")
        print("QR Code Data:", qr_data)
        return qr_data
    return None


def verify_student(image_path, Data):
    # Read the QR code
    qr_data = read_qr_code(image_path)

    # Verify student from the database
    if qr_data is not None:
        if qr_data in Data:
            student_name = Data[qr_data]
            print(f"Roll no.: {student_name['roll']}")
            print(f"Student Name: {student_name['name']}")
            print(f"Class: {student_name['class']}")
            print(f"Adress: {student_name['address']}")
        else:
            print("Student Not Found in Database")
    else:
        print("No QR Code Detected")



Data = load_database()
image_path = "Student QR.jpg"  # Replace with the actual image path
verify_student(image_path, Data)