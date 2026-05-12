import telebot
from flask import Flask
from threading import Thread

# --- ENGAÑO PARA RENDER ---
app = Flask('')
@app.route('/')
def home(): return "Bunker Activo"

def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

# --- TOKENS ---
TOKEN_DIRECTOR = '8665833044:AAF2Zs1CG8B4fl69-nLABXwbOn3XZ4StIL0'
bot = telebot.TeleBot(TOKEN_DIRECTOR)

@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text.lower()
    
    # --- SI BUSCAN DUDAS O NEGOCIO (AL GRUPO PRIVADO) ---
    if any(p in texto for p in ["duda", "ayuda", "luzia", "precio", "comprar", "mlc", "cuanto esta"]):
        bot.reply_to(message, "¡Oye asere! 🎓 Para dudas o negocios, entra a nuestro **Búnker Privado**: https://t.me/+Tzo4C3jek_QxNGUx. Ahí está la Secretaria Luzia esperando para darte la luz.")

    # --- SI BUSCAN DENUNCIAR A MANUEL (AL BOT DE SOPORTE) ---
    elif any(p in texto for p in ["estafa", "denuncia", "manuel", "facho", "robo", "acusacion"]):
        bot.reply_to(message, "¡🚨 ALERTA DE FACHO! Para reportar estafas o a los emisarios de Manuel, toca aquí: @SoporteCTECH_bot. ¡No vamos a dejar que nos embarren el búnker!")

    # --- SALUDO ---
    elif any(p in texto for p in ["hola", "que bola", "asere", "saludos"]):
        bot.reply_to(message, "¡Qué bolá! 🛡️ Aquí el Director. Estamos activos patrullando. Si vienes a aprender o a comprar, estás en el lugar correcto.")

if __name__ == "__main__":
    keep_alive()
    bot.polling()
