from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/test', methods=['GET', 'POST'])
def error():
    return render_template('test.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        url = request.form['url']
        if request.form['method']=='GET':
            try:
                response = requests.get(url)
                return render_template('result.html', response=response.text, title='Result')
            except requests.RequestException as e:
                return render_template('result.html', response=f"Error: {e}", title='Result')
        elif request.form['method']=='POST':
            url = request.form['url']
            data = request.form['data']
            try:
                response = requests.post(url, data=data)
                return render_template('result.html', response=response.text, title='Result')
            except requests.RequestException as e:
                return render_template('result.html', response=f"Error: {e}", title='Result')
    
    return render_template('index.html', title="Online HTTP Requester", response=True)

if __name__ == '__main__':
    app.run(debug=True)
