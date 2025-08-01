from flask import Flask, request, jsonify
#import jsonify to import json response

print ("code is now running dw")

app = Flask(__name__)  #create flask application

#creating the root, a root is an endpoint which is a location on the API
#to go to in order to retrieve some kind of data
#see other files for explanations of codes for routes in order of: simple, get, post


#GET route
@app.route("/get-user/<user_id>") 
def get_user(user_id):

    user_data = {
        "user_id": user_id,
        "name": "Muhammad Ahmed",
        "email": "muhammad.ahmed@example.com"
    }

    extra = request.args.get("extra") 

    
    if extra:
        user_data["extra"] = extra 

    return jsonify(user_data), 200  


#POST route
@app.route("/create-user", methods=["POST"])
def create_user():
    if request.method == "POST": 
    data = request.get_json() 

    return sjonify(data), 201   

'''
tests

http://127.0.0.1:5000/get-user/123?extra=extraIsWorkingJustFine  --> test the get


http://127.0.0.1:5000/create-user --> test the post via an API tester such as postman
'''



if __name__ == "__main__":  #running the app, basic initialisation
    app.run(debug=True)   #runs a flask server