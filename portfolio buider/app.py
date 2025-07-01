from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # Here you would normally process/store/send the message
    flash('Thank you for reaching out, {}!'.format(name))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)