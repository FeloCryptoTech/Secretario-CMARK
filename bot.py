import telebot
from flask import Flask
from threading import Thread

# --- EL ENGAÑO PARA RENDER ---
app = Flask('')
@app.route('/')
def home(): return "Bunker Activo"

def run(): app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

# TOKEN DEL DIRECTOR (El que está en Render)
TOKEN = '8665833044:AAF2Zs1CG8B4fl69-nLABXwbOn3XZ4StIL0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text.lower()
    
    # --- SI BUSCAN DUDAS O NEGOCIOS (Link del Grupo Privado que SÍ abre) ---
    if any(p in texto for p in ["duda", "ayuda", "luzia", "precio", "comprar", "mlc"]):
        bot.reply_to(message, "¡Oye asere! 🎓 Para dudas o negocios, entra a nuestro **Búnker Privado**: https://t.me/+Tzo4C3jek_QxNGUx. Ahí está la Secretaria Luzia lista.")

    # --- SI BUSCAN DENUNCIAR (Link del Soporte que SÍ abre) ---
    elif any(p in texto for p in ["estafa", "denuncia", "manuel", "facho"]):
        bot.reply_to(message, "¡🚨 ALERTA! Reporta al facho o la estafa aquí: @SoporteGlobal_bot. ¡No dejes que Manuel te engañe!")

    # --- SALUDO ---
    elif any(p in texto for p in ["hola", "que bola", "asere"]):
        bot.reply_to(message, "¡Qué bolá! 🛡️ Aquí el Director. El Búnker está echando candela. ¿Qué necesitas?")

if __name__ == "__main__":
    keep_alive()
    bot.polling()
