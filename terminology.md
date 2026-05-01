json: javaScript object notation
- a collection of key value pairs, similar to a python dictionary

jsonify
- puts data in json format
- whenever we returning data from an API, we'll be using json, user_data (example) is a dictionary which we've just jsonified (parsing the data)

query parameter
- essentially an extra value that is included after the path which can be added to the user_data


args
- stores query parameters in a dictionary


GET --> request data from a specifed resource, retrieve a value from the server
POST --> create a resource
PUT --> alter/mod/update a resource
DELETE  --> delete data from a resource e.g. from a db

---- there are others but there are the most common HTTP methods
--- methods are how we mark different api routes

Nology:

* API - Application Programming Interface *
- middleman between client/browser/app and data-sources/other services (maybe even another API?!)
- security guy

PATCH --> Partial update
PUT --> If entry doesn't exist, create. Else, replace.

CRUD --> cre, re, up, del --> Restful API 

12 - app uses method to api
21 - json/xml back to app




