from flask import Flask, render_template, request
from shioaji_helper import login_shioaji
import pandas as pd

app = Flask(__name__)
api = login_shioaji()

# 中文欄位對照字典
columns_translation = {
    'update_time': '更新時間',
    'system': '類別',
    'stock_id': '商品代碼',
    'margin_unit': '資餘額',
    'short_unit': '券餘額'
}

@app.route('/credit/<stock_code>')
def display_credit(stock_code):
    contracts = [api.Contracts.Stocks[stock_code]]
    credit_enquires = api.credit_enquires(contracts)
    df = pd.DataFrame(c.__dict__ for c in credit_enquires)
    df.update_time = pd.to_datetime(df.update_time)
    stock_name = api.Contracts.Stocks[stock_code].name
    
    # 將欄位名稱轉換成中文
    df.rename(columns=columns_translation, inplace=True)

    html_table = df.to_html(index=False)
    return render_template('credit.html', table=html_table, stock_name=stock_name)

if __name__ == '__main__':
    app.run(debug=True)
