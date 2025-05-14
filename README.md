
# TheBroadcaster360

A simple web dashboard built with Flask that lets an admin write a message in a browser and broadcast it to all subscribed users on Telegram via a bot.  

## Features

- Subscribe: Users send `/start` to your Telegram bot to subscribe.
- Broadcast: Admin logs into a web page and sends a message to _all_ subscribers in one click.
- Lightweight: Uses SQLite for storage, no external database required.
- Configurable: All secrets & settings live in an `.env` file.

---

## 🔧 Requirements

- OS: Windows 11 (or any OS with Python & Git)
- Python: ≥ 3.10  
- Git: for cloning & pushing to GitHub
- Telegram Bot Token: obtained from [BotFather](https://t.me/BotFather)
- Network: outbound HTTPS (to reach `api.telegram.org`)

---

## 🚀 Installation

1. Clone this repository  
   ```
   git clone https://github.com/hutrisemendawai/TheBroadcaster360.git
   cd TheBroadcaster360
   ```


2. Create & activate a virtual environment

   ```bash
   python -m venv venv
   .\venv\Scripts\activate       # Windows PowerShell
   # source venv/bin/activate    # macOS/Linux
   ```

3. Install Python dependencies

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. Create your `.env` file
   Copy the example and fill in your own values:

   ```bash
   copy .env.example .env        # Windows
   # cp .env.example .env       # macOS/Linux
   ```

   Edit `.env` and set:

   ```dotenv
   BOT_TOKEN=123456:ABC-DEF…         # your Telegram bot token
   ADMIN_USERNAME=admin             # your admin login username
   ADMIN_PASSWORD=strong_password   # your admin login password
   DATABASE_URL=sqlite:///broadcaster.db
   FLASK_ENV=development
   FLASK_DEBUG=1
   ```

5. Ensure `.gitignore` excludes

   * `venv/`
   * `*.db`
   * `.env`

---

## ▶️ Running the App

```bash
# Activate venv if not already active
.\venv\Scripts\activate

# Start the Flask + Bot polling
python app.py
```

By default, the app listens on:

* Web UI:  `http://127.0.0.1:5000/`
* Telegram Bot:  your bot will start polling automatically

---

## 📖 Usage

1. Subscribe

   * In Telegram, search your bot (`@YourBotUsername`), send `/start`.
   * You should receive a “You’re subscribed” confirmation.

2. Broadcast

   * Open the web UI: `http://127.0.0.1:5000/`
   * Log in with `ADMIN_USERNAME`/`ADMIN_PASSWORD`.
   * Type your message, click Send to All Subscribers.
   * All subscribers receive your broadcast instantly.

---

## 📂 Project Structure

```
TheBroadcaster360/
├── app.py                 # Main Flask + Telegram bot code
├── requirements.txt       # Python dependencies
├── .env.example           # Template for your .env configuration
├── .gitignore             # Excludes venv, .env, DB files, etc.
└── templates/
    └── home.html          # Admin broadcast page
```

---

## 🔒 Security & Deployment

* Never commit your real `.env` file to GitHub.
* For production, consider:

  * Using a real database (PostgreSQL/MySQL).
  * Serving via a WSGI server (Gunicorn/Uvicorn) behind Nginx.
  * Securing with HTTPS & strong secrets.
  * Switching from polling to webhooks for better reliability.

---

## 🤝 Contributing

Feel free to open issues or submit Pull Requests.
Please follow the existing code style and add tests where appropriate.

---

© 2025 TheBroadcaster360 

```
```
