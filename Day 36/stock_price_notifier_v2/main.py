
import os
from notifier import notify_all
from stock_checker import get_price_change
from news_fetcher import fetch_related_news

TICKER = os.getenv("TICKER", "TSLA")
THRESHOLD = float(os.getenv("THRESHOLD", 5.0))

def main():
    current_price, prev_close, change_percent = get_price_change(TICKER)
    if change_percent is None:
        print("❌ Not enough data.")
        return

    print(f"{TICKER} change: {change_percent:.2f}%")

    if abs(change_percent) >= THRESHOLD:
        direction = "↑" if change_percent > 0 else "↓"
        message = f"{TICKER} is {direction} {abs(change_percent):.2f}% today!\nPrice: {current_price:.2f}"
        headlines = fetch_related_news(TICKER)
        for article in headlines:
            message += f"\n- {article.get('title', '')}"
        notify_all(message)

if __name__ == "__main__":
    main()
