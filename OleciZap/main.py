from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#funcionalidade de enviar mensagens
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

#criar a primeira rota
@app.route("/")
def homepage():
    return render_template("btb.html")


#roda o aplicativo
if __name__ == "__main__":
    socketio.run(app)