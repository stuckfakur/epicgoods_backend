import mysql.connector
from mailjet_rest import Client
import os

# Ambil nilai dari variabel lingkungan
host = os.getenv('DB_HOST')
database = os.getenv('DB_DATABASE')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')

# Buat koneksi
def connection_check():
    try:
        connection = mysql.connector.connect(
            host=host,
            database=database,
            user=username,
            password=password
        )
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record[0])

    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        # Tutup koneksi jika sudah selesai
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# test email
def test_send_email():
    sender_email = os.getenv('EMAIL_USER')
    sender_name = "Me"
    recipient_email = os.getenv('EMAIL_RECEIPIENT')
    recipient_name = "You"

    api_key = os.getenv('MJ_APIKEY_PUBLIC')
    api_secret = os.getenv('MJ_APIKEY_PRIVATE')
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": sender_email,
                    "Name": sender_name
                },
                "To": [
                    {
                        "Email": recipient_email,
                        "Name": recipient_name
                    }
                ],
                "TemplateID": 12197550,
                "TemplateLanguage": True,
                "Subject": "My first Mailjet Email!",
                "TextPart": "Greetings from Mailjet!",
                "HTMLPart": "<h3>Dear passenger 1, welcome to <a href=\"https://www.mailjet.com/\">Mailjet</a>!</h3><br />May the delivery force be with you!"
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())