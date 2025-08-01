from flask import Flask, request, jsonify
#import jsonify to import json response

print ("code is now running dw")

app = Flask(__name__)  #create flask application

#creating the root, a root is an endpoint which is a location on the API
#to go to in order to retrieve some kind of data

'''
#this will be a simple route
@app.route("/")       #decorator using app name, / is the name of the route to be accessed which will be the default route
#the route would in reality be the URL accessed
def home(): #function for the root
    return "Home"  #any data for the user to access when they reach this route
'''

'''
GET --> request data from a specifed resource, retrieve a value from the server
POST --> create a resource
PUT --> alter/mod/update a resource
DELETE  --> delete data from a resource e.g. from a db

---- there are others but there are the most common HTTP methods
--- methods are how we mark different api routes

#json means sj obj notation

'''

#this will be a get route
@app.route("/get-user/<user_id>")  #this time with a path parameter <user_id> , dynamic value that can be passed in the path of a URL which can be accesed inside of our root
def get_user(user_id):
#"/get-user/4747" would indcate u want the data for user with the ID 4747
    user_data = {
        "user_id": user_id,
        "name": "Muhammad Ahmed",
        "email": "muhammad.ahmed@example.com"
    }

    extra = request.args.get("extra") 
    #accessing the query variable from flask, request was imported from flask, args stores query parameters in a dictionary, .get accesses the value such as extra
    
    if extra: #presence check
        user_data["extra"] = extra #stores the extra details
    
    return jsonify(user_data), 200  #returns data with response code of 200 (default status code of success, there are other HTTP status codes u can use but thats for another day to learn)
    #whenever we returning data from an API, we'll be using json
    #user_data is a dictionary which we've just jsonified (parsing the data)

#whenever we are accesing a route, we can pass a "query parameter" which is essentally
#an extra value that is included after the path
#e.g.   "get-user/123?extra=hello world"
#the question mark enables query parameters, extra is now an additional variable passed to the route



if __name__ == "__main__":  #running the app, basic initialisation
    app.run(debug=True)   #runs a flask server