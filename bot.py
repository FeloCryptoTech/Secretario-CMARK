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

# --- CONFIGURACIÓN ---
TOKEN = '8665833044:AAF2Zs1CG8B4fl69-nLABXwbOn3XZ4StIL0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text.lower()
    
    # 1. PARA PREGUNTAS DE PRECIO / NEGOCIO (El link nuevo que me diste)
    if any(p in texto for p in ["precio", "comprar", "vender", "cuanto esta", "mlc", "cup", "usd", "usdt"]):
        bot.reply_to(message, "¡Oye asere! 💎 Si vas a cuadrar un negocio o quieres saber el precio real al momento, entra aquí: https://t.me/soporteglobal")

    # 2. PARA DUDAS TÉCNICAS O LUZIA (Al búnker privado)
    elif any(p in texto for p in ["duda", "ayuda", "luzia", "binance", "p2p"]):
        bot.reply_to(message, "¡Tranquilo, fiera! 🎓 Si tienes dudas con el P2P o quieres hablar con la secretaria Luzia, entra aquí: https://t.me/+Tzo4C3jek_QxNGUx")

    # 3. PARA ESTAFAS O ACUSACIONES (El bot de soporte)
    elif any(p in texto for p in ["estafa", "denuncia", "manuel", "facho", "robo"]):
        bot.reply_to(message, "¡🚨 ALERTA! Si te trataron de estafar o viste un facho de Manuel, repórtalo rápido aquí: @SoporteGlobal_bot. ¡A esos no les damos tregua!")

    # 4. SALUDO NORMAL
    elif any(p in texto for p in ["hola", "que bola", "asere", "saludos"]):
        bot.reply_to(message, "¡Qué bolá! 🛡️ Bienvenido al Búnker. Estamos activos patrullando.")

if __name__ == "__main__":
    keep_alive()
    bot.polling()
