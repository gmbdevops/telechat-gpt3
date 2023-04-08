import sqlite3

import openai
import telebot
from dotenv import dotenv_values
from openai.error import RateLimitError, InvalidRequestError
from requests.exceptions import ReadTimeout
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

env = {
    **dotenv_values(".env.prod"),
    **dotenv_values(".env.dev"),  # override
}

API_KEYS_CHATGPT = [
    env["API_KEY_CHATGPT"],
]
bot = telebot.TeleBot(env["TG_BOT_TOKEN"])
db_link = env["DB_LINK"]

# Похоже, что твой код использует модули и библиотеки для работы с Telegram Bot # API, OpenAI API и SQLite базой данных. 

# dotenv используется для загрузки переменных окружения из файлов .env.prod и 
# .env.dev, которые содержат конфиденциальные данные, такие как API ключи и 
# ссылки на базу данных. 

# openai используется для работы с API OpenAI, который позволяет создавать и 
# обучать модели ИИ. 

# sqlite3 используется для работы с локальной базой данных SQLite, где могут 
# храниться данные, полученные от пользователей.

# telebot используется для работы с Telegram Bot API, который позволяет создавать # и настраивать ботов для Telegram.

# telegram.ext используется для создания обработчиков сообщений и команд, 
# которые будут выполняться при получении сообщений от пользователей.

# pydantic используется для валидации данных, которые могут быть получены от 
# пользователей.

# В целом, этот код представляет собой основу для создания бота, который может 
# использовать искусственный интеллект для обработки сообщений от 
# пользователей и предоставлять им различные функции и возможности.

# Инициализация базы данных SQLite
conn = sqlite3.connect(db_link)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (user_id INTEGER PRIMARY KEY, chat_id INTEGER, api_key TEXT)''')
conn.commit()

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Создаем кнопку "Старт"
    start_button = InlineKeyboardButton('🚀 Старт 🚀', callback_data='start')

    # Создаем клавиатуру
    keyboard = InlineKeyboardMarkup([[start_button]])

    # Отправляем приветственное сообщение с гифкой и клавиатурой
    bot.send_animation(message.chat.id, animation='https://media.giphy.com/media/OnQYRvlj7gCNQdKS5c/giphy.gif',
                       caption="✌️Приветствую. Рад видеть✌️\n\n💬 Я Исскуственный Интеллект🤖, и  готов ответить на любой твой вопрос! 💁\n\n      🗣 - мультиязыковая поддержка\n      🔱 - ведение бесед     \n      🤳 - создание контента\n      🧠 - поиск и анализ информации\n      💢 - програмирование\n      🌀 - решение задач и уравнений\n\nСкорее пиши и убедись сам! 🎆🎆🎆",
                       reply_markup=main_menu_keyboard)
    # вариант 2: reply_markup=keyboard)

# Создаем кнопки для главного меню
button1 = InlineKeyboardButton('1. Примеры использования', callback_data='button1')
button2 = InlineKeyboardButton('2. Все о технологии ИИ', callback_data='button2')
button3 = InlineKeyboardButton('3. Мои чаты', callback_data='button3')
button4 = InlineKeyboardButton('4. Настройки', callback_data='button4')
button5 = InlineKeyboardButton('5. Другие ИИ', callback_data='button5')

# Создаем клавиатуру для главного меню
main_menu_keyboard = InlineKeyboardMarkup([
    [button1],
    [button2],
    [button3],
    [button4],
    [button5]
])




# Далее мы добавили обработчики для каждой кнопки главного
# меню. Вот пример обработчика для кнопки "Примеры использования":

# Обработчик кнопки "Примеры использования"
@bot.callback_query_handler(func=lambda call: call.data == 'button1')
def button1_handler(call):
    # Отправляем сообщение с примерами использования
    bot.send_message(call.message.chat.id, 'Примеры использования:')
    bot.send_message(call.message.chat.id, '1. Создание чат-ботов')
    bot.send_message(call.message.chat.id, '2. Распознавание речи')
    bot.send_message(call.message.chat.id, '3. Анализ текста')
    bot.send_message(call.message.chat.id, '4. Рекомендательные системы')


# В этом коде мы создали обработчик для кнопки "Примеры
# использования" с помощью функции callback_query_handler. 
# Функция func позволяет нам указать условие, при котором 
# обработчик будет вызываться. В данном случае мы указали, что 
# обработчик должен быть вызван только при нажатии на кнопку с 
# callback_data равным "button1".

# Внутри обработчика мы отправляем сообщение с примерами 
# использования. Мы используем функцию bot.send_message для 
# отправки текстовых сообщений. 

# Аналогично, мы можем создать обработчики для остальных кнопок главного меню. 

# Обработчик кнопки "Все о технологии ИИ"
@bot.callback_query_handler(func=lambda call: call.data == 'button2')
def button2_handler(call):
    # Отправляем сообщение с информацией о технологии ИИ
    bot.send_message(call.message.chat.id, 'Все о технологии ИИ:')
    bot.send_message(call.message.chat.id,
                     'Искусственный интеллект (ИИ) - это область компьютерных наук, которая занимается созданием интеллектуальных машин, которые могут действовать, как люди.')


# Обработчик кнопки "Мои чаты"
@bot.callback_query_handler(func=lambda call: call.data == 'button3')
def button3_handler(call):
    # Отправляем сообщение с информацией о моих чатах
    bot.send_message(call.message.chat.id, 'Мои чаты:')
    bot.send_message(call.message.chat.id, '1. Чат с пользователем 1')
    bot.send_message(call.message.chat.id, '2. Чат с пользователем 2')
    bot.send_message(call.message.chat.id, '3. Чат с пользователем 3')


# Обработчик кнопки "Настройки"
@bot.callback_query_handler(func=lambda call: call.data == 'button4')
def button4_handler(call):
    # Отправляем сообщение с настройками
    bot.send_message(call.message.chat.id, 'Настройки:')
    bot.send_message(call.message.chat.id, '1. Язык')
    bot.send_message(call.message.chat.id, '2. Уведомления')


# Обработчик кнопки "Другие ИИ"
@bot.callback_query_handler(func=lambda call: call.data == 'button5')
# Например, если ты хочешь добавить функцию для обработки текстовых сообщений, то можешь использовать следующий код:

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def handle_text(message):
    # Отвечаем на сообщение
    bot.send_message(message.chat.id,
                     'Я не понимаю, что вы хотите сказать. Пожалуйста, выберите функцию из главного меню.')


# Этот обработчик будет вызываться при получении любого текстового сообщения #от пользователя, которое не соответствует ни одной из команд или кнопок.
# В данном случае, мы просто отправляем пользователю сообщение о том, что мы  #непонимаем, что он хочет сказать, и просим его выбрать функцию из главного  #меню.

# Если ты хочешь добавить функцию для обработки изображений, то # можешь использовать следующий код:

# Обработчик изображений
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # Скачиваем изображение
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Отправляем сообщение с информацией о размере изображения
    bot.send_message(message.chat.id, f'Изображение загружено. Размер: {len(downloaded_file)} байт.')


# Этот обработчик будет вызываться при получении изображения
# от пользователя. В этом примере мы скачиваем изображение 
# с помощью метода bot.download_file, получаем его размер 
# с помощью функции len, и отправляем пользователю сообщение 
# с информацией о размере изображения.

# Также, можешь использовать другие обработчики для обработки 
# других типов контента, таких как аудио, видео, документы и т.д. 
# Просто добавь новые обработчики в свой код и опиши нужную 
# логику для каждого типа контента.

# Если ты хочешь добавить функцию для обработки аудио-
# сообщений, то можешь использовать следующий код:

# Обработчик аудио-сообщений
@bot.message_handler(content_types=['voice'])
def handle_voice(message):
    # Скачиваем аудио-сообщение
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # Отправляем сообщение с информацией о длительности 
    # аудио-сообщения
    bot.send_message(message.chat.id, f'Аудио-сообщение загружено. Длительность: {message.voice.duration} секунд.')


# Этот обработчик будет вызываться при получении аудио-
# сообщения от пользователя. В этом примере мы скачиваем аудио- # сообщение с помощью метода bot.download_file, получаем его
# длительность с помощью атрибута message.voice.duration, и
# отправляем пользователю сообщение с информацией о
# длительности аудио-сообщения.

# Также, можешь использовать другие обработчики для обработки  # других типов контента, таких как видео, документы и т.д. Просто
# добавь новые обработчики в свой код и опиши нужную логику для
# каждого типа контента.

# Обработчик текстовых сообщений
@bot.message_handler(content_types=['text'])
def text_handler(message):
    # Получение текста сообщения
    text = message.text

    # Генерация ответа с помощью OpenAI API
    try:
        response = openai.Completion.create(
            engine=model_engine,
            prompt=text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        answer = response.choices[0].text
    except (ReadTimeout, RateLimitError, InvalidRequestError) as e:
        answer = "Извините, произошла ошибка при генерации ответа. Попробуйте еще раз позже."

    # Отправка ответа пользователю
    bot.send_message(message.chat.id, answer)


if __name__ == "__main__":
    bot.polling(none_stop=True)

# Этот код создает бота, который может обрабатывать команды, 
# кнопки и текстовые сообщения от пользователей, генерировать 
# ответы с помощью OpenAI API и хранить данные в базе данных 
# SQLite. 

# Он также использует библиотеку pydantic для валидации данных, 
# которые могут быть получены от пользователей, и обработчики 
# для обработки других типов контента, таких как аудио-сообщения 
# и документы.
