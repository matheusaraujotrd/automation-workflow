import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
user = os.getenv('USER', "user not set")
password = os.getenv('PASSWORD', "password not set")
