from flask import Flask, request, jsonify
import shioaji as sj
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize Shioaji API
api = sj.Shioaji(simulation=True)  # Simulation mode
api.login(
    api_key=os.getenv("API_KEY"),
    secret_key=os.getenv("SECRET_KEY")
)

app = Flask(__name__)

@app.route('/stock/<symbol>', methods=['GET'])
def get_stock(symbol):
    contract = api.Contracts.Stocks[symbol]
    return jsonify({"stock": str(contract)})

if __name__ == '__main__':
    app.run(debug=True)
