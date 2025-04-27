from flask import Flask, render_template, request, jsonify
from bot import ask_healthbot  
import time


app = Flask(__name__)
chat_history = [{"user": "", "bot": "Welcome to GynoBot!! Feel free to ask me any Health Queries."}]  

@app.route("/", methods=["GET"])
def index():
    return render_template("home.html", chat_history=chat_history)

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.form.get("user_input")
    bot_response = ask_healthbot(user_input)
    chat_history.append({"user": user_input, "bot": bot_response})
    return jsonify({"user_input": user_input, "bot_response": bot_response})

@app.route("/clear", methods=["POST"])
def clear():
    global chat_history
    chat_history = [{"user": "", "bot": "Welcome to GynoBot!! Feel free to ask me any Health Queries."}]
    return render_template("home.html", chat_history=chat_history)
    


if __name__ == "__main__":
    app.run(debug=True)
