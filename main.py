from flask import Flask, render_template
from random import choice
from data import mcq

app = Flask(__name__)
app.secret_key = "your_secret_key"

visited = []
question = ""
option1 = ""
option2 = ""
brief1 = ""
brief2 = ""
op1 = ""
op2 = ""


def update():
    data = choice(mcq)
    global question, option1, option2, brief1, brief2, op1, op2
    question = data["question"]
    option1 = data["option1"]
    option2 = data["option2"]
    brief1 = data["brief1"]
    brief2 = data["brief2"]
    if "right" in brief1:
        op1 = "right"
        op2 = "wrong"
    else:
        op1 = "wrong"
        op2 = "right"

    print(question, option1, option2, brief1, brief2, op1, op2)


update()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/1')
def first():
    update()
    return render_template('first.html', question=question, option1=option1, option2=option2)


@app.route('/e1')
def efirst():
    return render_template('e1.html', brief1=brief1, op1=op1)


@app.route('/c1')
def cfirst():
    return render_template('c1.html', brief2=brief2, op2=op2)


if __name__ == '__main__':
    app.run(debug=True)
