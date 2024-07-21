# BlogSphere

## Overview
BlogSphere is a blog website built with Django where users can view, create, edit, and delete blogs. Additionally, users can comment on others' blogs. The project incorporates Twilio for OTP authentication during login and signup to ensure secure user verification. The website also features a responsive design to provide an optimal viewing experience across different devices.

## Features
- User Authentication with OTP (Twilio)
- Create, Read, Update, and Delete (CRUD) Blogs
- Comment on Blogs
- Responsive Design
- User-friendly Interface

## Prerequisites
To run this project, you will need:
- Python
- Django
- Twilio account (for OTP authentication)

## Installation

1. **Clone the repository**
    ```bash
    git clone https://github.com/Priyanshu2sh/Blog-Sphere.git
    cd Blog-Sphere/BlogSphere
    ```

2. **Create and activate a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Twilio**
    - Create a [Twilio account](https://www.twilio.com/try-twilio).
    - Register a phone number with Twilio.
    - Get your `account_sid`, `auth_token`, and Twilio phone number.

5. **Configure Twilio credentials in settings.py**
    - Open the `settings.py` file and update the following variables with your Twilio credentials:
        ```python
        TWILIO_ACCOUNT_SID = 'your_account_sid'
        TWILIO_AUTH_TOKEN = 'your_auth_token'
        TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
        ```

6. **Apply migrations**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Run the server**
    ```bash
    python manage.py runserver
    ```

8. **Access the application**
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Twilio Setup
To use Twilio for OTP authentication:
- Sign up for a Twilio account.
- Verify your phone number with Twilio.
- Retrieve your `account_sid`, `auth_token`, and registered Twilio phone number.
- Update these credentials in the `settings.py` file as mentioned above.

For more information, refer to the [Twilio documentation](https://www.twilio.com/docs).

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. Your contributions are always welcome!

## Demo
Here is a demo video of the project: [Watch Demo Video](https://drive.google.com/file/d/17CJHmCc8ctxZUaT-aIilgoUau30wZeoD/view?usp=drive_link)

Happy Blogging with BlogSphere!
