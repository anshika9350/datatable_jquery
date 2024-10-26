from flask import Flask, request, jsonify
from db import*

app = Flask(__name__)


@app.route('/api/data', methods=['POST'])
def receive_data():
    obj=DB()
    data = request.get_json()  # Get the JSON data from the request
    print(data) # Print data to console or process it as needed
    obj.insertion(data['user_id'],data['name'],data['email'],data['category'])
    return jsonify({"message": "Data received successfully!"}), 200

@app.route('/api/get', methods=['GET'])
def get_user():
    obj=DB()
    result = obj.get_users()
    return jsonify(
        {"message": "Data received successfully!",
         'data' : result}), 200
    
@app.route('/api/newdata', methods=['POST'])
def updated_data():
    obj=DB()
    newdata = request.get_json()
    print(newdata)  
    obj.update_users(newdata['new_category'],newdata['user_id2'])
    return jsonify({"message": "Data received successfully!"}), 200

if __name__ == '__main__':
    app.run(debug=True)

