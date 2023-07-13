import qrcode
def generate_qr_code(data, file_path):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(file_path)
data = input("Enter student data for QR code...\n")  # Replace with the actual data you want to encode
file_path = "Student QR.jpg"  # Replace with the desired file path and name
generate_qr_code(data, file_path)


print("Done!!")
