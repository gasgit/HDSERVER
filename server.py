from flask import Flask, request
from flask import json
import pprint


# test server for HelpDesk App on the same network
# turn off data 
# host on 0.0.0.0 to allow detection on network




app = Flask(__name__)

@app.route('/api', methods=['POST'])
def api():
    if request.headers['Content-Type'] == 'application/json':
        if request.method == 'POST':      
            data = json.dumps(request.json)
            parsed = json.loads(data)
            print json.dumps(parsed, indent=4)
               
    return '0k'





@app.route('/api/hello', methods=['GET','POST'])
def api_hello():
    if request.method == 'GET':
    
        return "Hello From Flask!!"

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
