QR Code Generator

A simple Django web application that generates QR codes for URLs.

The user enters a name and URL. The application creates a QR code image for that URL and displays the generated QR code on a result page.

Features

Generate a QR code from any valid menu URL

Enter a name to create a descriptive QR-code filename

Validate the name and URL using a Django form

Save generated QR-code images in the media/ directory

Display the generated QR code using a Django template

Bootstrap-based frontend

Technologies Used

Python

Django 6.1.1

Python qrcode library

Pillow

SQLite

HTML

Bootstrap 5

Project Structure

backend/
├── backend/
│   ├── __init__.py
│   ├── asgi.py
│   ├── forms.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── media/
│   └── Generated QR-code images
├── templates/
│   ├── generate_qr_code.html
│   └── qr_result.html
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md

The local virtual environment, SQLite database, generated media, cache files, and environment variables are excluded from Git by the existing .gitignore.

How It Works

Open the application in a browser.

Enter a name.

Enter the URL.

Submit the form.

Django validates the input.

The qrcode package generates a QR code for the supplied URL.

The image is saved in the media/ directory.

The result page displays the generated QR code.

Generated files follow this naming pattern:

name_menu.png

For example:

Sai Restaurant

produces:

sai_restaurant_menu.png

Prerequisites

Make sure you have:

Python 3.12+ installed

pip installed

Git installed if you want to upload the project to GitHub

Installation

1. Clone the repository

git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd backend

If you are working with the project locally without cloning it, simply open a terminal in the project directory.

2. Create a virtual environment

Windows:

python -m venv env
env\Scripts\activate

macOS/Linux:

python3 -m venv env
source env/bin/activate

3. Install dependencies

pip install -r requirements.txt

The project currently uses these main packages:

Django==6.1.1
qrcode==8.2
Pillow==12.3.0

If your local requirements.txt was saved in UTF-16 and pip install -r requirements.txt reports an encoding error, save the file as UTF-8 and run the command again.

4. Apply Django migrations

python manage.py migrate

5. Start the development server

python manage.py runserver

Open:

http://127.0.0.1:8000/

Usage

On the home page:

Enter the name in the QR Name field.

Enter the URL in the URL field.

Click the submit/generate button.

The generated QR code will be shown on the result page.

Scan the QR code with a phone camera or QR scanner to open the menu URL.

URL Validation

The application uses Django's URLField, so the submitted URL must be a valid URL.

Example:

https://example.com/menu

Generated Files

QR-code images are stored under:

media/

The project is configured to serve these files during local development.

For example:

media/
└── sai_restaurant_menu.png



Author
Saikiranreddy
