from flask import Flask, request, render_template, jsonify
# i imported from flask a request library that i will use to request the message
# render template is for updating the html template atumatic 
# and jsonify is for the data base 

app = Flask(__name__)

@app.route('/') # מציין שהפונקצייה תטפל בבקשות GET שמגיעות לכתובת הראשית
def index():
    return render_template('index.html')  # Renders the HTML page from the templates folder

@app.route('/', methods=['POST'])
def receive_message():
    message = request.json.get('message', '')
    print(f"Received message: {message}")
    return jsonify({"status": "Message received", "message": message})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
