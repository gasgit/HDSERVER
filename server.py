from flask import Flask, request
from flask import json
import pprint



app = Flask(__name__)

@app.route('/api', methods=['POST'])
def hello_world():
    if request.headers['Content-Type'] == 'application/json':
        if request.method == 'POST':      
            data = json.dumps(request.json)
            parsed = json.loads(data)
            print json.dumps(parsed, indent=4)
               
    return '0k'





@app.route('/api/hello', methods=['GET','POST'])
def hello():
    if request.method == 'GET':
    
        return "Hello From Flask!!"

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)