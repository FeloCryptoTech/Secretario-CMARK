import telebot
from flask import Flask
from threading import Thread
import time

# --- SERVIDOR PARA RENDER ---
app = Flask('')
@app.route('/')
def home(): return "Bunker C-MARK Activo"

def run(): app.run(host='0.0.0.0', port=10000)

# --- CONFIGURACIÓN DE DAINIER ---
TOKEN = '8665833044:AAEd4roGPBw8uPlUMCSWTIM6BLmrJSV9-s0'
bot = telebot.TeleBot(TOKEN, threaded=False)

@bot.message_handler(func=lambda message: True)
def responder(message):
    try:
        t = message.text.lower().strip()
        
        # 1. NEGOCIOS Y PRECIOS
        if any(p in t for p in ["precio", "cuanto", "valor", "mlc", "usd", "usdt", "cup", "compro", "vendo"]):
            bot.reply_to(message, "¡Oye asere! 💎 Si quieres saber el precio o cuadrar un negocio, camina para la oficina: https://t.me/soporteglobal")

        # 2. AYUDA / ERRORES / P2P (Nueva Oficina: @SoporteGlobal_bot)
        elif any(p in t for p in ["ayuda", "error", "p2p", "no sale", "luzia", "dainier", "transfer", "codigo", "sms"]):
            bot.reply_to(message, "¡Tranquilo! 🎓 Si tienes líos con el P2P o una transferencia, escribe a @luzia. Si ella no lo resuelve, yo mismo (Dainier) te atiendo en mi nueva oficina: @SoporteGlobal_bot. ¡Dale suave que todo tiene solución!")

        # 3. MALAS PALABRAS
        elif any(p in t for p in ["coño", "pinga", "carajo", "mierda", "pendejo"]):
            bot.reply_to(message, "Amigo, relaja. Entendemos el estrés, pero respeta el búnker. Habla con @luzia para ayudarte, o ven a mi nueva oficina: @SoporteGlobal_bot. ¡Aquí resolvemos!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    bot.remove_webhook()
    time.sleep(1)
    print("Dainier patrullando con la nueva oficina: @SoporteGlobal_bot...")
    bot.infinity_polling(skip_pending=True)
