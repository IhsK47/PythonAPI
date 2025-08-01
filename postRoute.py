#POST route
@app.route("/create-user", methods=["POST"]) #since we're not using the default get request we have to specify the method for the route, POST means allow post, we could also add ,"GET" into the array,
def create_user():
    if request.method == "POST": #check which method, so could elif to GET etc | since post is the only method, this line is kind of redundant
    data = request.get_json()  #receive data from the req that will be in JSON format which will be the data of the user they want to create

    #this line would update the db but this is a simple demo API so our code won't do that

    return sjonify(data), 201   #return this to the user to idicate it was successful


'''
#Testing

    http://127.0.0.1:5000/create-user --> test the post via an API tester such as postman
'''
