from flask import Flask, render_template, request
from shioaji_helper import login_shioaji
import pandas as pd

app = Flask(__name__)
api = login_shioaji()

# 中文欄位對照字典
columns_translation = {
    'ts': '時間',
    'close': '成交價',
    'volume': '成交量',
    'bid_price': '委買價',
    'bid_volume': '委買量',
    'ask_price': '委賣價',
    'ask_volume': '委賣量',
    'tick_type': '內外盤別'
}

# 中文tick_type對照字典
tick_type_translation = {
    1: '外盤',
    2: '內盤',
    0: '無法判定'
}

@app.route('/ticks/<stock_date>/<stock_code>')
def display_ticks(stock_date, stock_code):
    ticks = api.ticks(
        contract=api.Contracts.Stocks[stock_code], 
        date=stock_date
    )
    stock_name = api.Contracts.Stocks[stock_code].name

    df = pd.DataFrame({**ticks})
    df.ts = pd.to_datetime(df.ts)
    
    # 將欄位名稱轉換成中文
    df.rename(columns=columns_translation, inplace=True)
    
    # 將tick_type的數字轉換成中文表示
    df['內外盤別'] = df['內外盤別'].map(tick_type_translation)
    
    html_table = df.to_html(index=False, escape=False, classes='table table-striped')  # escape=False，以顯示HTML樣式
    return render_template('index.html', table=html_table, stock_name=stock_name)

if __name__ == '__main__':
    app.run(debug=True)
