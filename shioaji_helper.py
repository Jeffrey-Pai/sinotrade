# shioaji_helper.py

import shioaji as sj
from dotenv import load_dotenv
import os

def login_shioaji():
    # Load environment variables from .env file
    load_dotenv()

    # Initialize Shioaji API
    api = sj.Shioaji(simulation=True)  # Simulation mode
    api.login(
        api_key=os.getenv("API_KEY"),
        secret_key=os.getenv("SECRET_KEY")
    )

    return api
