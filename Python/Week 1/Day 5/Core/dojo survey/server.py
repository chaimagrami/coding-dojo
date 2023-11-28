from flask import Flask, render_template, request,redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        session['name'] = request.form['name']
        session['DojoLocation'] = request.form['DojoLocation']
        session['FavoriteLanguage'] = request.form['FavoriteLanguage']

        # Display form data on the result page
        return redirect('/result')

    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)
