from flask import Blueprint, request, render_template,jsonify
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
            data = request.form['data']
            response = postData(url, data)
            return render_template('index.html', response=response, title='Result')
    
    return render_template('index.html', title="Online HTTP Requester", response=False)
 
@views.route('/submit', methods=['POST'])
def handle_form():
    # Extract data from form data
    username = request.form.get('username')
    email = request.form.get('email')
    
    # Check if the necessary data is present
    if not username or not email:
        return jsonify({"error": "Missing username or email"}), 400  # Bad Request

    # Concatenate the received data
    concatenated_data = f"Username: {username}, Email: {email}"
    
    # Respond with the concatenated data and a 200 OK status
    return jsonify({"message": concatenated_data}), 200
