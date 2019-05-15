import utils.configs as configs
import flask
import telebot
import time
from utils.news_generator import ITNewsGenerator, ImprovedITNewsGenerator

HELP_STRING = """
I suppose, you'd like to get amazing article from me. Today you're very lucky.
Choose any theme:
/it
/improved_it - more powerful algorithm
/political
"""

bot = telebot.TeleBot(configs.TOKEN)

app = flask.Flask(__name__)


@app.route(configs.WEBHOOK_URL_PATH, methods=["POST"])
def webhook():
    if flask.request.headers.get("content-type") == "application/json":
        json_string = flask.request.get_data().decode("utf-8")
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


@bot.message_handler(commands=["start"])
def start_command(message):
    bot.reply_to(message, "Hello, friend! My name is Journalissst.")


@bot.message_handler(commands=["help"])
def send_help(message):
    bot.send_message(message.chat.id, HELP_STRING)


@bot.message_handler(commands=["it"])
def send_it_news(message):
    bot.send_message(message.chat.id, ITNewsGenerator().generate(50))


@bot.message_handler(commands=["improved_it"])
def send_improved_it_news(message):
    bot.send_message(message.chat.id, ImprovedITNewsGenerator().generate(50))


@bot.message_handler(commands=["political"])
def send_political_news(message):
    bot.send_message(message.chat.id, "Sorry, but I lied. I can't write \
                                       political articles now.")


bot.remove_webhook()

time.sleep(1)

bot.set_webhook(url=configs.WEBHOOK_URL_BASE + configs.WEBHOOK_URL_PATH,
                certificate=open(configs.WEBHOOK_SSL_CERT, 'r'))

if __name__ == "__main__":
    app.run(host=configs.WEBHOOK_LOCAL_HOST,
            port=configs.WEBHOOK_PORT,
            ssl_context=(configs.WEBHOOK_SSL_CERT, configs.WEBHOOK_SSL_PRIV))
