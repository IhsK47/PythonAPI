#GET route
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




#whenever we are accesing a route, we can pass a "query parameter" which is essentially
#an extra value that is included after the path
#e.g.   "get-user/123?extra=hello world"
#the question mark enables query parameters, extra is now an additional variable passed to the route


'''
Testing

http://127.0.0.1:5000/get-user/

http://127.0.0.1:5000/get-user/123?extra=hello

#you can put absolutely anything after the = sign





'''