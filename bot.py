import telebot
import os  # ESTO ES NUEVO
from flask import Flask
from threading import Thread
import time

app = Flask('')
@app.route('/')
def home(): return "Bunker C-MARK Activo"

def run(): app.run(host='0.0.0.0', port=10000)

# --- AQUÍ ESTÁ EL TRUCO DE SEGURIDAD ---
# Ya no ponemos el número del token aquí, lo lee de Render
TOKEN = os.environ.get('BOT_TOKEN') 
bot = telebot.TeleBot(TOKEN, threaded=False)

@bot.message_handler(func=lambda message: True)
def responder(message):
    try:
        t = message.text.lower().strip()
        # (Aquí van tus reglas de "precio", "ayuda", etc., iguales que antes)
        if any(p in t for p in ["precio", "cuanto", "mlc", "usd"]):
            bot.reply_to(message, "¡Oye asere! 💎 Oficina aquí: https://t.me/soporteglobal")
        elif any(p in t for p in ["ayuda", "error", "p2p", "luzia"]):
            bot.reply_to(message, "¡Tranquilo! 🎓 Escribe a @luzia o ven a mi oficina: @SoporteGlobal_bot")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    bot.remove_webhook()
    time.sleep(1)
    bot.infinity_polling(skip_pending=True)
