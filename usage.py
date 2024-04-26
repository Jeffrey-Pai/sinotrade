from flask import Flask, render_template
from shioaji_helper import login_shioaji
import pandas as pd

app = Flask(__name__)
api = login_shioaji()

@app.route('/usage', methods=['GET'])
def get_usage():
    # 使用你的 API 函數獲取數據
    usage_data = api.usage()

    # 將數據傳遞到模板
    return render_template('usage.html', usage_data=usage_data)
# def display_ticks(stock_date, stock_code):
    start_time = time.time()  # 開始時間
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
    end_time = time.time()  # 結束時間
    execution_time = end_time - start_time  # 執行時間
    print(f"執行時間：{execution_time} 秒")
    return render_template('ticks.html', table=html_table, stock_name=stock_name)
if __name__ == '__main__':
    app.run(debug=True)
