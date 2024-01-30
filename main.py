from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        try:
            response = requests.get(url)
            return render_template('result.html', response=response.text)
        except requests.RequestException as e:
            return render_template('result.html', response=f"Error: {e}")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
