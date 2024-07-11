from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({ 'mensagem': 'Hello world, RENAPSI' })


@app.route('/user')
def user():
    return jsonify([
        { 'name': 'John Doe', 'idade': 30 },
        { 'name': 'Jane Doe', 'idade': 25 }
    ])

if __name__ == '__main__':
   app.run()