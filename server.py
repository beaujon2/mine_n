# server.py

from flask import Flask
from threading import Thread
from mine2 import run_bot

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot Dice actif 24h/24 🚀"

def run():
    app.run(host='0.0.0.0', port=8080)

# Lancer le serveur Flask et le bot Telegram en parallèle
if __name__ == '__main__':
    Thread(target=run).start()
    run_bot()
