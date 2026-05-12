import telebot
from flask import Flask
from threading import Thread

# --- SERVIDOR ---
app = Flask('')
@app.route('/')
def home(): return "Bunker Activo"

def run(): app.run(host='0.0.0.0', port=8080)

# --- CONFIGURACIÓN ---
TOKEN = '8665833044:AAF2Zs1CG8B4fl69-nLABXwbOn3XZ4StIL0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def responder(message):
    # Limpiamos el texto para que no importe mayúsculas, tildes o espacios
    t = message.text.lower().strip()
    
    # 1. INTENCIÓN: PRECIOS Y NEGOCIOS (Cubre: "a como esta", "precio", "usd", "mlc", "cuanto vale", etc.)
    if any(p in t for p in ["precio", "cuanto", "valor", "mlc", "usd", "usdt", "cup", "vale", "quien vende", "compro"]):
        bot.reply_to(message, "¡Oye asere! 💎 Si quieres saber el precio real ahora mismo o cuadrar un negocio seguro, camina para nuestra oficina: https://t.me/soporteglobal")

    # 2. INTENCIÓN: FALLOS, AYUDA Y P2P (Cubre: "ayuda", "error", "no sale", "transferi", "no me llega", "no veo", "p2p")
    elif any(p in t for p in ["ayuda", "ayude", "error", "transfer", "no sale", "p2p", "no llega", "no veo", "codigo", "sms", "falta"]):
        bot.reply_to(message, "¡Tranquilo, fiera! 🎓 Si el P2P te dio error, la transferencia no sale o el código no llega, no te desesperes. La conexión a veces se pone lenta. Escribe ahora mismo a **@luzia** (nuestra Secretaria) para que ella revise tu caso. Si la cosa es muy técnica, ella te pasará con nuestro colega Dainier aquí: https://t.me/SoporteCTECH_bot. ¡Dale suave que todo se resuelve!")

    # 3. INTENCIÓN: SEGURIDAD (Cubre: "estafa", "manuel", "facho", "robo", "engañaron")
    elif any(p in t for p in ["estafa", "manuel", "facho", "robo", "engañe", "mentira"]):
        bot.reply_to(message, "¡🚨 ALERTA! Si viste un movimiento raro o un facho, repórtalo rápido aquí: @SoporteGlobal_bot. ¡Aquí no andamos con cuentos!")

    # 4. MANEJO DE MALEDUCADOS (Detección de malas palabras comunes)
    elif any(p in t for p in ["coño", "pinga", "carajo", "pendejo", "estafa", "mierda"]):
        bot.reply_to(message, "Amigo, entendemos tu frustración y será un placer ayudarte, pero por favor, aquí no estás solo y los demás usuarios no tienen la culpa. Le pedimos disculpas si hubo un error en la plataforma, a veces la conexión se pone pesada. Camina con Luzia escribiendo **@luzia** para que ella te atienda primero, y si hace falta, ella te pone en cola con Dainier (https://t.me/SoporteCTECH_bot). ¡Relaja, que aquí resolvemos!")

    else:
        pass

if __name__ == "__main__":
    t = Thread(target=run)
    t.start()
    bot.remove_webhook()
    bot.infinity_polling(skip_pending=True)
