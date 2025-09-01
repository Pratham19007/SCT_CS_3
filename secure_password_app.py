from flask import Flask, render_template, request
from password_strength import assess_password_strength

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    strength = None
    details = None
    password = ''
    if request.method == 'POST':
        password = request.form.get('password', '')
        strength, details = assess_password_strength(password)
    return render_template('secure_password.html', strength=strength, details=details, password=password)

if __name__ == '__main__':
    app.run(debug=True)