from flask import Flask, render_template, request, jsonify
from interfaces.web.controllers.email_controller import EmailController
from config.settings import DEBUG

app = Flask(__name__,
    template_folder='interfaces/web/templates',
    static_folder='interfaces/web/static')

email_controller = EmailController()

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/process-email', methods=['POST'])
def process_email():
    return email_controller.process_email()

if __name__ == '__main__':
    app.run(debug=DEBUG, host='0.0.0.0', port=5000)