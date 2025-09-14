#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24201237"))
API_HASH = environ.get("API_HASH", "fc82db3f86816844f36abd55bf218b12")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "1202075632"))
CREDIT = environ.get("CREDIT", "mahi")
AUTH_USER = os.environ.get('AUTH_USERS', '5680454765').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER)
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8090)) # Default to 8000 if not set


