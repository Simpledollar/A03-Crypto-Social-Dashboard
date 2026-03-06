from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Giá trị khởi tạo tạm thời, sẽ được cập nhật qua JS từ Binance API
    prices = {
        "BTC": 0,
        "ETH": 0,
        "SOL": 0,
        "BNB": 0,
        "DOGE": 0,
    }
    return render_template("index.html", prices=prices)

if __name__ == "__main__":
    app.run(debug=True)
