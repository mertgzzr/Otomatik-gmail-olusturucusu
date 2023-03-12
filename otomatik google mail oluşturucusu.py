import google.auth
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import random
import string

# Google API kimlik doğrulama bilgileri
creds = Credentials.from_authorized_user_file('path/to/credentials.json')

# Gmail API istemcisini oluştur
service = build('gmail', 'v1', credentials=creds)

# Gmail hesabı oluşturma fonksiyonu
def create_gmail_account(first_name, last_name, password):
    try:
        # Ad ve soyadı kullanarak e-posta adresi oluştur
        username = (first_name + '.' + last_name).lower() + ''.join(random.choices(string.digits, k=3))
        email = username + '@gmail.com'

        # Gmail hesabı oluşturma isteği
        user = {
            'email': email,
            'password': password
        }
        request = service.users().create(profile=user, body=user).execute()

        # Başarı mesajı yazdır
        print(f"Gmail hesabı başarıyla oluşturuldu. E-posta adresi: {email}")
    except HttpError as error:
        # Hata mesajı yazdır
        print(f"Gmail hesabı oluşturulamadı. Hata: {error}")

# Gmail hesabı oluştur
first_name = "John"
last_name = "Doe"
password = "123456789"
create_gmail_account(first_name, last_name, password)
