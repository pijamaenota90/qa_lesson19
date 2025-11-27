import os

from dotenv import load_dotenv

load_dotenv()

user_name = os.getenv('USER_NAME')
access_key = os.getenv('ACCESS_KEY')
remote_url = os.getenv('REMOTE_URL')

