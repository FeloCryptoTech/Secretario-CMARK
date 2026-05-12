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

TOKEN = '8665833044:AAF2Zs1CG8B4fl69-nLABXwbOn3XZ4StIL0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text.lower()
    
    # --- DEPARTAMENTO DE DUDAS (SOPORTE PRIVADO CON LUZIA) ---
    palabras_dudas = ["duda", "ayuda", "ayudame", "no entiendo", "luzia", "binance", "p2p", "problema"]
    if any(p in texto for p in palabras_dudas):
        bot.reply_to(message, "¡Oye asere! 🎓 Si tienes dudas técnicas o quieres hablar con nuestra **Secretaria General Luzia**, entra aquí a nuestro soporte privado: https://t.me/+Tzo4C3jek_QxNGUx. Ahí hay privacidad total y el Antivirus está activo. 🛡️")

    # --- DEPARTAMENTO DE ACUSACIONES (EL BOT DE SOPORTE) ---
    elif any(p in texto for p in ["estafa", "denuncia", "acusacion", "manuel", "facho", "robo", "engaño"]):
        bot.reply_to(message, "¡Atención! 🚨 Si vienes a denunciar una estafa o un movimiento de los hijos de #*@ de Manuel, repórtalo directo aquí: https://t.me/SoporteCTECH_bot. Vamos a darle fuego a los estafadores.")

    # --- DINERO Y PRECIOS ---
    elif any(p in texto for p in ["precio", "comprar", "vender", "cuanto esta", "mlc", "cup"]):
        bot.reply_to(message, "¡Qué bolá! 💎 Para cuadrar negocios al momento, entra al soporte de dudas: https://t.me/+Tzo4C3jek_QxNGUx. Ahí te atendemos rápido.")

if __name__ == "__main__":
    keep_alive()
    bot.polling()
