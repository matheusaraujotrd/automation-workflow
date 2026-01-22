import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
user = os.getenv('USER', "user not set")
password = os.getenv('PASSWORD', "password not set")
login_url = os.getenv('LOGIN_URL', "login url not set")
home_url = os.getenv('HOME_URL', "home url not set")
create_account_url = os.getenv('CREATE_ACCOUNT_URL', "create account url not set")
forgot_password_url = os.getenv('FORGOT_PASSWORD_URL', "forgot password url not set")
service_terms_url = os.getenv('SERVICE_TERMS_URL', "service terms url not set")
privacy_policy_url = os.getenv('PRIVACY_POLICY_URL', "privacy policy url not set")