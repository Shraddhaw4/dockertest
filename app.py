from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
 
@app.route('/login')
def login():
    return render_template('login.html')
 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("3000"), debug=True)