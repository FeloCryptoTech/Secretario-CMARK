import telebot
import os
from flask import Flask
from threading import Thread

# --- EL ENGAÑO PARA RENDER ---
app = Flask('')
@app.route('/')
def home():
    return "Bunker Activo"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ----------------------------

TOKEN = '8665833044:AAF2Zs1CG8B4fl69-nLABXwbOn3XZ4StIL0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text.lower()
    if any(p in texto for p in ["precio", "comprar", "vender", "cuanto esta", "pago", "mlc", "cup", "tarjeta", "transferencia", "usd", "usdt"]):
        bot.reply_to(message, "¡Oye, asere! 💎 Si vas a cuadrar una operación o quieres saber el precio al momento, toca aquí: https://t.me/SoporteCTECH_bot")
    elif any(p in texto for p in ["ayuda", "ayudame", "tengo duda", "no entiendo", "problema", "bloqueo", "binance", "okx", "red", "trc20", "estafa", "facho", "respondeme"]):
        bot.reply_to(message, "¡Tranquilo, fiera! 🎓 Para esa duda técnica o ese enredo con el P2P, escribe @luzia y hazle la pregunta. Ella sabe de eso, pero no de las mipymes de la Habana jjjj.")
    elif any(p in texto for p in ["hola", "buenas", "que bola", "asere", "saludos"]):
        bot.reply_to(message, "¡Qué bolá! 🛡️ Bienvenido al Búnker C-MARK. Estamos activos.")

if __name__ == "__main__":
    keep_alive()
    bot.polling()
