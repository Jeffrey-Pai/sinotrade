import shioaji as sj
from dotenv import load_dotenv
import os
# 載入 .env 文件中的變數
load_dotenv()

api = sj.Shioaji(simulation=True) # 模擬模式
api.login(
    api_key=os.getenv("API_KEY"),    
    secret_key=os.getenv("SECRET_KEY")   
)
stock1 = api.Contracts.Stocks["2890"]
print(stock1)
