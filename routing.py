from flask import Blueprint, request, render_template,jsonify
from utils import getData, postData

views = Blueprint('views', __name__)

@views.route('/test', methods=['GET', 'POST'])
def error():
    return render_template('test.html')

@views.route('/', methods=['GET', 'POST'])
def index(): 
    return render_template('index.html', title="Online HTTP Requester")
 
@views.route('/submit', methods=['POST'])
def handle_form():
    url = request.form.get('url')
    method = request.form.get('method')
    if(method == 'GET'):
        response = getData(url)
    elif(method == 'POST'):
        response = postData(url, request.form.get('data'))
    if not url or not method:
        return jsonify({"error": "Missing username or email"}), 400 
    return jsonify({"message": response}), 200
