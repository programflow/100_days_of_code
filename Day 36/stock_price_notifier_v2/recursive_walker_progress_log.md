
# 🐍 Modular Stock Price Notifier with Signal + SMS

This project monitors a stock ticker (e.g., TSLA) and sends you a notification via Signal or SMS if the price changes beyond a specified threshold.

## 📁 Project Structure

```
.
├── main.py              # Orchestrates price check, news fetch, and notifications
├── notifier.py          # Sends alerts via Signal or SMS (using carrier email)
├── stock_checker.py     # Uses yfinance to calculate % change in price
├── news_fetcher.py      # Pulls top 3 news articles about the ticker (NewsAPI)
├── .env                 # Stores secrets and configuration
```

## ⚙️ Configuration (.env file)

Create a `.env` file in the same directory with:

```ini
MY_EMAIL=your_email@gmail.com
MY_PASSWORD=your_email_app_password
MY_PHONE=+15555555555
SIGNAL_UUID=+15555555555
NEWS_API_KEY=your_newsapi_key
TICKER=TSLA
THRESHOLD=5
CARRIER=spectrum
```

- `SIGNAL_UUID` can be your registered number (if using Signal CLI primary identity).
- Supported carriers: `spectrum`, `verizon`, `tmobile`.

## 🧠 How It Works

1. `main.py` loads your ticker and threshold from `.env`.
2. It uses `stock_checker.py` to get current and previous close prices.
3. If price change exceeds the threshold:
   - It uses `news_fetcher.py` to pull related news.
   - It formats a message and calls `notifier.notify_all()`.
4. `notifier.py` will send the message via Signal (preferred) or fallback to SMS if configured.

## 🚀 Running It

```bash
python main.py
```

## ✅ Tips

- Set this up as a cronjob to check daily
- Add logging to record sent alerts
- Add multiple tickers or thresholds in `main.py`
