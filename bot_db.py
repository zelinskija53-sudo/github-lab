import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot("8883942720:AAF6xx6cCm_4Svgr9S2tLZIDImZ2INxfVFc")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('мат+физика')
    btn2 = types.KeyboardButton('мат+информатика')
    btn3 = types.KeyboardButton('химия+биология')
    keyboard.add(btn1, btn2, btn3)
    
    bot.send_message(
        message.chat.id, 
        "Привет! Я бот для поиска вузов Самары.\nВыбери свои предметы по выбору на клавиатуре ниже, и я найду подходящие варианты напрямую из базы данных:", 
        reply_markup=keyboard
    )

@bot.message_handler(content_types=['text'])
def find_university(message):
    exam_request = message.text.lower()
    
    try:
        # Подключаемся к базе данных
        conn = sqlite3.connect('vyzi.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT Name, Score, Description FROM Universities WHERE Exam = ?", (exam_request,))
        results = cursor.fetchall()
        
        if results:
            response = "🎓 Найденные вузы в базе данных:\n\n"
            for row in results:
                response += f"🏛 {row[0]}\n📊 Проходной балл: от {row[1]}\nℹ️ {row[2]}\n\n"
            bot.send_message(message.chat.id, response)
        else:
            bot.send_message(message.chat.id, "Пожалуйста, воспользуйтесь кнопками меню для поиска.")
            
    except sqlite3.Error as e:
        bot.send_message(message.chat.id, f"⚠️ Ошибка БД. Проверь, что vyzi.db лежит в одной папке с ботом. Ошибка: {e}")
    finally:
        if 'conn' in locals() and conn:
            conn.close()

print("Бот запускается... Пожалуйста, подождите пару секунд.")
bot.infinity_polling(timeout=20, long_polling_timeout=15)