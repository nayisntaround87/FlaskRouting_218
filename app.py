from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Memanggil file HTML bernama index.html

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return render_template('submit.html', name=name)  # Memanggil submit.html dengan parameter
    return render_template('form.html')  # Memanggil form.html jika metode GET

if __name__ == '__main__':
    app.run(debug=True)