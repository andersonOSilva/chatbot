#import files
from flask import Flask, render_template, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

app = Flask(__name__)


bot = ChatBot("Candice")
bot.set_trainer(ListTrainer)
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")



@app.route("/")
def home():
    return jsonify({"message": "Bem vindo ao BOT. Utilize o ENDPOINT '/get?msg=SUA MSG AQUI' para falar com o bot "})

@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')
    return jsonify({"response": str(bot.get_response(userText)) })


if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5000)
    
    
    #bot.get_response(userText)