from flask import Flask, render_template, 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('start.html', content=hey())

def hey():
    return 'bruh'

if __name__ == '__main__':
    app.run(debug=True)