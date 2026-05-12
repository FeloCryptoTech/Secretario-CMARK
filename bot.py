import telebot
from flask import Flask
from threading import Thread
import time

# --- SERVIDOR PARA RENDER ---
app = Flask('')
@app.route('/')
def home(): return "Bunker C-MARK Activo"

def run(): app.run(host='0.0.0.0', port=8080)

# --- CONFIGURACIÓN DE DAINIER CON TOKEN NUEVO ---
TOKEN = '8665833044:AAEd4roGPBw8uPlUMCSWTIM6BLmrJSV9-s0'
bot = telebot.TeleBot(TOKEN, threaded=False)

@bot.message_handler(func=lambda message: True)
def responder(message):
    try:
        t = message.text.lower().strip()
        print(f"Dainier leyendo en tiempo real: {t}")

        # REGLA 1: NEGOCIOS Y PRECIOS
        if any(p in t for p in ["precio", "cuanto", "valor", "mlc", "usd", "usdt", "cup", "vale", "compro", "vendo"]):
            bot.reply_to(message, "¡Oye asere! 💎 Si quieres saber el precio o cuadrar un negocio, camina para la oficina: https://t.me/soporteglobal")

        # REGLA 2: AYUDA / ERRORES / P2P
        elif any(p in t for p in ["ayuda", "error", "p2p", "no sale", "luzia", "dainier", "transfer", "codigo", "sms"]):
            bot.reply_to(message, "¡Tranquilo! 🎓 Si tienes líos con el P2P o una transferencia, escribe a **@luzia**. Si ella no lo resuelve, yo mismo (Dainier) te atiendo en mi oficina: https://t.me/SoporteCTECH_bot")

        # REGLA 3: MALAS PALABRAS / FRUSTRACIÓN
        elif any(p in t for p in ["coño", "pinga", "carajo", "mierda", "pendejo"]):
            bot.reply_to(message, "Amigo, relaja. Entendemos el estrés, pero respeta el búnker. Habla con **@luzia** para ayudarte, o ven a mi oficina con Dainier aquí: https://t.me/SoporteCTECH_bot")

    except Exception as e:
        print(f"Error en respuesta: {e}")

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    
    # LIMPIEZA DE CONEXIÓN
    print("Limpiando conexiones viejas...")
    bot.remove_webhook()
    time.sleep(1) 
    
    print("Director (Dainier) Patrullando con Token Nuevo...")
    # El skip_pending=True es para que no se vuelva loco con los mensajes que enviaste ahora
    bot.infinity_polling(skip_pending=True)
