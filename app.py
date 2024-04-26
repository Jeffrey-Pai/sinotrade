from flask import Flask, request, jsonify
from shioaji_helper import login_shioaji

app = Flask(__name__)
api = login_shioaji()

@app.route('/stock/<symbol>', methods=['GET'])
def get_stock(symbol):
    contract = api.Contracts.Stocks[symbol]
    return jsonify({"stock": str(contract)})

if __name__ == '__main__':
    app.run(debug=True)
