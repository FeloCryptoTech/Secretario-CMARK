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

# --- CONFIGURACIÓN ---
TOKEN = '8665833044:AAF2Zs1CG8B4fl69-nLABXwbOn3XZ4StIL0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def responder(message):
    # Pasamos todo a minúsculas para que no haya fallo
    t = message.text.lower()
    
    # 1. DUDAS DE PRECIO Y VALOR (Solo frases clave)
    if any(frase in t for frase in ["precio de", "cuanto vale", "a como esta", "precio del"]):
        bot.reply_to(message, "¡Oye asere! 💎 Si quieres saber el precio real al momento o cuadrar un negocio, entra aquí: https://t.me/soporteglobal")

    # 2. DUDAS DE TRANSFERENCIA Y P2P (Problemas técnicos)
    elif any(frase in t for frase in ["como transfiero", "ayude", "ayuda", "transferencia no sale", "entrar al p2p", "no entiendo"]):
        bot.reply_to(message, "¡Tranquilo! 🎓 Para temas de transferencias, dudas con el P2P o hablar con Luzia, entra a nuestro privado: https://t.me/+Tzo4C3jek_QxNGUx")

    # 3. SEGURIDAD (Si mencionan al facho de Manuel o estafas)
    elif any(frase in t for frase in ["estafa", "manuel", "facho", "robo", "me engañaron"]):
        bot.reply_to(message, "¡🚨 ALERTA! Si viste un movimiento raro o un facho, repórtalo rápido aquí: @SoporteGlobal_bot. ¡Guerra avisada no mata soldado!")

    # SI NO ES NINGUNA DE ESAS, EL DIRECTOR SE QUEDA CALLADO.
    else:
        pass

if __name__ == "__main__":
    keep_alive()
    bot.polling()
