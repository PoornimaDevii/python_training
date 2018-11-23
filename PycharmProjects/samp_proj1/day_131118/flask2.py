from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>/<int:eid>')
def hello_name(name,eid):
    return 'Hello %s!! Your emp ID is %d!' %(name,eid)

@app.route('/hi/<name>')
def hi_name(name):
    return 'Hi %s!!' %name

if __name__ == '__main__':
    app.run(debug=True)