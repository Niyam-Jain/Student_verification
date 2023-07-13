# Student Verification Using QR Code

This project is a simple implementation of student verification using QR codes. It allows you to scan a QR code containing student information and verify it against a database. The project is written in Python and utilizes the following libraries:

- `cv2` (OpenCV): A computer vision library used for image processing and manipulation.
- `pyzbar`: A library for detecting and decoding various types of barcodes, including QR codes.
- `PIL` (Python Imaging Library): A library for opening, manipulating, and saving many different image file formats.
- `json`: A built-in Python module for working with JSON data.

## Installation and Setup

To run this project, you need to have Python installed on your system. You can download the latest version of Python from the official Python website: https://www.python.org/downloads/

After installing Python, follow these steps to set up the project:

1. Download or clone the project files to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Install the required Python libraries by running the following command:
```
pip install opencv-python pyzbar pillow
```
4. Make sure you have a QR code image containing student information. Replace the `image_path` variable in the code with the actual path to your QR code image.

## Usage

Once you have set up the project, you can use it to verify student information using QR codes. Follow these steps:

1. Prepare a QR code image containing student information.
2. Run the Python script `student_verification.py`.
3. The script will load the student database from the `student_database.json` file.
4. It will then read the QR code from the provided image and decode its data.
5. If a valid QR code is detected, the script will check if the student exists in the database.
6. If the student is found, it will display the student's roll number, name, class, and address.
7. If the student is not found or no QR code is detected, appropriate messages will be displayed.

Ensure that you have properly configured the `student_database.json` file with the relevant student information before running the script.

## Customization

To customize the project for your needs, you can make the following modifications:

- **Database**: Update the `student_database.json` file with the student information you want to verify. The file should be in JSON format with QR code data as keys and student details as values.
- **QR Code Image**: Replace the `image_path` variable in the code with the actual path to your QR code image.

Feel free to modify the code as per your requirements to extend its functionality or integrate it into your own projects.

## Acknowledgments

- The project utilizes the following open-source libraries: OpenCV, pyzbar, and PIL.
- Special thanks to the contributors of these libraries for their valuable work.

If you have any questions or suggestions, please feel free to contact me.

Enjoy using the Student Verification Using QR Code project!
