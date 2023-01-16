import telebot
from telebot import types
import requests
import random
import openai
import os

token = " " # YOUR TOKEN 
bot = telebot.TeleBot(token) 

commands = '''
Мои команды:

Искусственный интеллект - GPT3
ии / пример: ии what`s your name ?

Писать желательно на английском!

Очистить чат
"clear" или "очистить чат"
'''

def generate_response(prompt):
  completions = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.5,
  )

  message = completions.choices[0].text
  return message.strip()

@bot.message_handler(func=lambda message: True)
def solve_task(message):
    def msg(message_text):
        bot.send_message(message.chat.id, str(message_text))


    import openai

    ai = 'ai', 'ии'
    clear = 'clear', 'очистить чат'
    openai.api_key = " "  # YOUR API KEY OPENAI   https://beta.openai.com/signup/
    try:
        if message.text.lower().startswith(ai):
            text = message.text.split()

            del text[0]
            new_text = ' '.join(text)

            response = generate_response(prompt=new_text)

            bot.send_message(message.chat.id, response)

        elif message.text.lower().startswith(clear):
            new_message_id = message.message_id
            while new_message_id > 1:
                bot.delete_message(message.chat.id, new_message_id)
                new_message_id = new_message_id - 1

        elif message.text.lower() == '/start':
            user_nickname = message.from_user.username
            bot.send_message(message.chat.id, f'Здравствуйте, *{user_nickname}* !\nНапиши в чат "команды" чтобы посмотреть список моих команд.', parse_mode='Markdown')

        else:
            bot.send_message(message.chat.id, 'Я не знаю такую команду\n\nНапишите "команды" чтобы посмотреть список моих команд')
    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка!\n\n{e}')
bot.polling()