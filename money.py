from flask import Flask, render_template, request
from shioaji_helper import login_shioaji
import pandas as pd

app = Flask(__name__)
api = login_shioaji()

print(api.list_positions(api.stock_account))
