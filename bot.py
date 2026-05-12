import telebot
from flask import Flask
from threading import Thread

# --- SERVIDOR PARA RENDER ---
app = Flask('')
@app.route('/')
def home(): return "Bunker C-MARK Activo"

def run(): app.run(host='0.0.0.0', port=8080)

# --- CONFIGURACIÓN DE DAINIER ---
TOKEN = '8665833044:AAF2Zs1CG8B4fl69-nLABXwbOn3XZ4StIL0'
bot = telebot.TeleBot(TOKEN, threaded=False)

@bot.message_handler(func=lambda message: True)
def responder(message):
    try:
        t = message.text.lower().strip()
        print(f"Dainier leyendo: {t}") # Esto saldrá en Render

        # REGLA 1: NEGOCIOS
        if any(p in t for p in ["precio", "cuanto", "valor", "mlc", "usd", "usdt", "cup", "compro", "vendo"]):
            bot.reply_to(message, "¡Oye asere! 💎 Si quieres saber el precio o cuadrar un negocio, camina para la oficina: https://t.me/soporteglobal")

        # REGLA 2: AYUDA / ERRORES
        elif any(p in t for p in ["ayuda", "error", "p2p", "no sale", "luzia", "dainier", "transfer"]):
            bot.reply_to(message, "¡Tranquilo! 🎓 Si tienes líos con el P2P o una transferencia, escribe a **@luzia**. Si ella no lo resuelve, yo mismo (Dainier) te atiendo en mi oficina. Dale aquí: https://t.me/SoporteCTECH_bot")

        # REGLA 3: MALAS PALABRAS
        elif any(p in t for p in ["coño", "pinga", "carajo", "mierda"]):
            bot.reply_to(message, "Amigo, relaja. Entendemos el estrés, pero respeta el búnker. Habla con **@luzia** para ayudarte, o ven a mi oficina con Dainier aquí: https://t.me/SoporteCTECH_bot")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    bot.remove_webhook()
    print("Dainier patrullando el Búnker...")
    bot.infinity_polling(skip_pending=True)
