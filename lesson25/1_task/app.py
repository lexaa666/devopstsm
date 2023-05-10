from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Home page!"
@app.route("/get_answer", methods=["GET"])
def get_answer():
    return "This is the answer to the GET request."
@app.route("/post_answer", methods=["POST"])
def post_answer():
    data = request.get_json()
    return f"This is the answer to the POST request. Data received: {data}"
if __name__ == "__main__":
    app.run()