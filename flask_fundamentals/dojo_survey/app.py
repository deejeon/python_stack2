from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def save_result():
    dict = {}
    dict['name'] = request.form['name']
    dict['location'] = request.form['location']
    dict['language'] = request.form['language']
    dict['comment'] = request.form['comment']
    return render_template('result.html', context=dict)

if __name__ in "__main__":
    app.run(debug=True)