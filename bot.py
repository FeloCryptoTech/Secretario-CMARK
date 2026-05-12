import telebot
import time
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

# --- CONFIGURACIÓN DE MANDOS ---
TOKEN = '8665833044:AAF2Zs1CG8B4fl69-nLABXwbOn3XZ4StIL0'
bot = telebot.TeleBot(TOKEN)
ID_GRUPO = -1003600514698  # Tu ID de la Comunidad

# --- RELOJ DE PROPAGANDA (CADA 1 HORA) ---
def propaganda_seguridad():
    while True:
        try:
            mensaje = (
                "🚨 **¡BÚNKER C-MARK ACTIVO!** 🛡️\n\n"
                "Atención Comunidad, para su seguridad el Estado Mayor informa:\n\n"
                "1️⃣ **NEGOCIOS:** Para comprar o vender seguro, entren al Soporte Privado: https://t.me/+Tzo4C3jek_QxNGUx\n"
                "2️⃣ **DUDAS:** Nuestra Secretaria General **Luzia** está lista para guiarlos en privado.\n"
                "3️⃣ **SEGURIDAD:** El Antivirus **Nelson** y la Veterana **Rosy** están patrullando. No acepten tratos por fuera.\n\n"
                "⚠️ **¡EVITEN LAS ESTAFAS!** Reporten cualquier facho de Manuel a @SoporteGlobal_bot."
            )
            bot.send_message(ID_GRUPO, mensaje, parse_mode="Markdown")
        except Exception as e:
            print(f"Error en el envío: {e}")
        
        time.sleep(3600) # 3600 segundos = 1 Hora

# --- RESPUESTAS TÁCTICAS DEL DIRECTOR ---
@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text.lower()
    
    if any(p in texto for p in ["duda", "ayuda", "luzia", "precio", "comprar", "mlc"]):
        bot.reply_to(message, "¡Oye asere! 🎓 Para dudas o negocios, entra al Búnker Privado: https://t.me/+Tzo4C3jek_QxNGUx. Ahí está Luzia.")

    elif any(p in texto for p in ["estafa", "denuncia", "manuel", "facho", "nelson", "rosy"]):
        bot.reply_to(message, "¡🚨 ALERTA! Nelson y Rosy están al tanto. Reporta cualquier movimiento extraño aquí: @SoporteGlobal_bot")

    elif any(p in texto for p in ["hola", "que bola", "asere"]):
        bot.reply_to(message, "¡Qué bolá! 🛡️ Aquí el Director reportándose. La Comunidad está blindada.")

if __name__ == "__main__":
    keep_alive()
    # Arranca el reloj de 1 hora en segundo plano
    Thread(target=propaganda_seguridad).start()
    bot.polling()
