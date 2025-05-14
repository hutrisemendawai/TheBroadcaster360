import os
import threading
import asyncio
import requests
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_basicauth import BasicAuth
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'password')
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///thebroadcaster360.db')

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=DATABASE_URL,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    BASIC_AUTH_USERNAME=ADMIN_USERNAME,
    BASIC_AUTH_PASSWORD=ADMIN_PASSWORD,
    BASIC_AUTH_FORCE=False
)

db = SQLAlchemy(app)
basic_auth = BasicAuth(app)

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chat_id = db.Column(db.BigInteger, unique=True, nullable=False)

with app.app_context():
    db.create_all()

application = ApplicationBuilder().token(BOT_TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    with app.app_context():
        subscription = Subscriber.query.filter_by(chat_id=chat_id).first()
        if not subscription:
            db.session.add(Subscriber(chat_id=chat_id))
            db.session.commit()
            message = "✅ You’re subscribed to TheBroadcaster360!"
        else:
            message = "👍 You’re already subscribed."
    await context.bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')

application.add_handler(CommandHandler('start', start))

def run_telegram():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    application.run_polling()

if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
    threading.Thread(target=run_telegram, daemon=True).start()

@app.route('/', methods=['GET', 'POST'])
@basic_auth.required
def broadcast():
    success = None
    if request.method == 'POST':
        msg = request.form.get('message', '').strip()
        if msg:
            subscribers = Subscriber.query.all()
            for sub in subscribers:
                requests.get(
                    f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage',
                    params={'chat_id': sub.chat_id, 'text': msg}
                )
            success = f"🎉 Message sent to {len(subscribers)} subscribers."
    return render_template('home.html', success=success)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
