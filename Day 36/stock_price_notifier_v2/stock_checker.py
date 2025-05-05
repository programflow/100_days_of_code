
import yfinance as yf

def get_price_change(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="2d")

    if len(data) < 2:
        return None, None, None

    prev_close = data['Close'].iloc[-2]
    current_price = data['Close'].iloc[-1]
    change_percent = ((current_price - prev_close) / prev_close) * 100

    return current_price, prev_close, round(change_percent, 2)
