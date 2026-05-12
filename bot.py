import telebot

# CONFIGURACIÓN DEL DIRECTOR C-MARK
TOKEN = '8665833044:AAF2Zs1CG8B4fl69-nLABXwbOn3XZ4StIL0'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def responder(message):
    texto = message.text.lower()
    
    # --- SECCIÓN DE DINERO Y PRECIOS (DIRECTO A SOPORTE) ---
    palabras_soporte = ["precio", "comprar", "vender", "cuanto esta", "pago", "mlc", "cup", "tarjeta", "transferencia", "usd", "usdt"]
    if any(p in texto for p in palabras_soporte):
        bot.reply_to(message, "¡Oye, asere! 💎 Si vas a cuadrar una operación o quieres saber el precio al momento, toca aquí: https://t.me/SoporteCTECH_bot. Ahí te damos la luz rápido.")

    # --- SECCIÓN DE DUDAS P2P Y AYUDA TÉCNICA (A LUZIA) ---
    elif any(p in texto for p in ["ayuda", "ayudame", "tengo duda", "no entiendo", "problema", "bloqueo", "binance", "okx", "red", "trc20", "estafa", "facho", "respondeme"]):
        bot.reply_to(message, "¡Tranquilo, fiera! 🎓 Para esa duda técnica o ese enredo con el P2P, llama a nuestra experta: escribe @luzia y hazle la pregunta. Ella sabe más que un libro abierto, de lo que no sabe ella es de las mipymes de la Habana jjjj.")

    # --- BIENVENIDA Y SALUDOS ---
    elif any(p in texto for p in ["hola", "buenas", "que bola", "asere", "saludos"]):
        bot.reply_to(message, "¡Qué bolá! 🛡️ Bienvenido al Búnker C-MARK. Aquí estamos activos. Si necesitas aprender, pregunta; si necesitas comprar, toca el link de soporte.")

bot.polling()
