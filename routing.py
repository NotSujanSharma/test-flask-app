from flask import Blueprint, request, render_template
from utils import getData, postData

views = Blueprint('views', __name__)

@views.route('/test', methods=['GET', 'POST'])
def error():
    return render_template('test.html')

@views.route('/', methods=['GET', 'POST'])
def index(): 
    if request.method == 'POST':
        url = request.form['url']
        if request.form['method']=='GET':
            response = getData(url)
            return render_template('index.html', response=response, title='Result')
        elif request.form['method']=='POST':
            url = request.form['url']
            data = request.form['data']
            response = postData(url, data)
            return render_template('index.html', response=response, title='Result')
    
    return render_template('index.html', title="Online HTTP Requester", response=False)
 
