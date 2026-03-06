from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,binancecoin,dogecoin&vs_currencies=usd"
    data = requests.get(url).json()
    prices = {
        "BTC": data.get("bitcoin", {}).get("usd", 0),
        "ETH": data.get("ethereum", {}).get("usd", 0),
        "SOL": data.get("solana", {}).get("usd", 0),
        "BNB": data.get("binancecoin", {}).get("usd", 0),
        "DOGE": data.get("dogecoin", {}).get("usd", 0),
    }
    return render_template("index.html", prices=prices)

if __name__ == "__main__":
    app.run(debug=True)
