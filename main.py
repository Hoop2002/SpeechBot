import telebot
from config import token
import textHandler

client = telebot.TeleBot(token)


@client.message_handler(commands=['start'])
def start_message(message):
    client.send_message(message.from_user.id, "Привет, я бот, который поможет тебе перевести текст в речь\n"
                                              "Напиши сюда любой текст на русской языке:")

    print(f"________________________________\n"
          f"Пользватель: {message.from_user.first_name}\n"
          f"Прислал сообщение: {message.text} ")


@client.message_handler(content_types=["text"])
def get_message(message):
    if message.text is not None:
        client.send_message(message.from_user.id, "Ожидайте, идет обработка...")

        textHandler.speech_creator(message.text)
        audio_file = open(r"VoiceDocuments\file.mp3", "rb")

        client.send_document(message.from_user.id, document=audio_file)

        print(f"________________________________\n"
              f"Пользватель: {message.from_user.first_name}\n"
              f"Прислал сообщение: {message.text} ")


if __name__ == "__main__":
    print("[bot started]")
    client.polling(none_stop=True, interval=0)
