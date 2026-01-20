import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
user = os.getenv('USER', "user not set")
password = os.getenv('PASSWORD', "password not set")
login_url = os.getenv('LOGIN_URL', "login url not set")
home_url = os.getenv('HOME_URL', "home url not set")