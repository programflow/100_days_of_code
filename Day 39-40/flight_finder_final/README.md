# ✈️ Cheap Flight Finder

This project checks for flight deals based on your preferences and notifies you when ticket prices drop below your set threshold.

It uses the Amadeus API to fetch flight data, Sheety to store user preferences in Google Sheets, and Signal CLI and email to notify you when deals are found.

---

## 🔧 Features

- ✅ Read flight preferences from a Google Sheet
- ✅ Automatically complete missing IATA codes
- ✅ Check flight prices over a rolling 6-month window
- ✅ Alert via Signal and Email when deals are found
- ✅ Environment-variable driven config
- ✅ Modular and refactor-friendly code structure

---

## 🚀 Setup

1. **Clone the repo**  
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create your `.env` file** (see below)  
4. **Link your Signal device** using `signal-cli`  
5. **Run the project**
   ```bash
   python main.py
   ```

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory:

```env
# Amadeus API credentials
AMADEUS_API=your_amadeus_api_key
AMADEUS_SECRET=your_amadeus_secret_key

# Sheety API endpoints
SHEETY_PRICES_ENDPOINT=https://api.sheety.co/...
SHEETY_USERS_ENDPOINT=https://api.sheety.co/...

# Gmail credentials
MY_EMAIL=youremail@example.com
MY_PASSWORD=your_gmail_app_password

# Signal CLI credentials
SIGNAL_PHONE=+11234567890
SIGNAL_UUID=your-linked-device-uuid
```

---

## 🛠 Usage

1. Add destinations and price thresholds to your Sheety-connected Google Sheet.
2. Add customer emails (optional) to receive email alerts.
3. Run `main.py` to start the deal-checking pipeline.
4. If deals are found, you’ll get messages like:

```
📢 Low price alert!
NYC (JFK) → LON (LHR)
💰 Price: $249
🛫 Outbound: 2025-07-14
🛬 Inbound: 2025-07-21
```

---

## ⏱ Automation (Optional)

You can run the script on a schedule using `cron`:

```bash
0 7 * * * /usr/bin/python3 /path/to/main.py
```

---

## 📬 Notification Channels

- **Signal**: Requires `signal-cli` and linked device UUID.
- **Email**: Uses Gmail’s SMTP service with app password.

---

## 📁 License

MIT License © 2025 Kevin Floort