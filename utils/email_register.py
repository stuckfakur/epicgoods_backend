import os

from mailjet_rest import Client


def send_email(recipient_email, recipient_name):
    sender_email = os.getenv('EMAIL_USER')
    sender_name = "Epic Goods"

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
                "Subject": "Successful Register on EpiGoods!",
                "TextPart": "Thanks for registering!",
                "HTMLPart": "<h3>Dear {recipient_name}, welcome to <a "
                            "href=\"https://www.mailjet.com/\">Mailjet</a>!</h3><br />May the delivery force be with "
                            "you!".format(recipient_name=recipient_name)
            }
        ]
    }
    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
