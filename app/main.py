from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/", methods=['POST'])
def requestPrint():
    headersOut = request.headers.to_list()
    response = {
        "headers" : headersOut,
        "body" : request.json
    } 
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
