from google import genai
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
client = genai.Client(api_key="AIzaSyDxd5y6UqLWs_uMW1WJd5zPz7NgOctSIKY")
app = Flask(__name__)

#? Create Routes
@app.route("/") #? home route
def home(): return jsonify({'message':"My Own API!"})

@app.route("/<prompt>", methods=["GET"])
def prompt(prompt):
    response = client.models.generate_content(
        model="gemma-4-26b-a4b-it",
        contents=prompt
    )
    return jsonify({"response":response})

# @app.route("/des", methods=["GET"]) #? destinations route, with GET method
# def get_des(): #? this is to link that endpoint with this function
#     destinations = Destination.query.all()
#     return jsonify([des.toDict() for des in destinations])
# #* http://127.0.0.1:5000/des OR in practice: http://127.0.0.1:5000/des

# @app.route("/des/<int:des_id>", methods=["GET"])
# def get_des_id(des_id):
#     destination =  Destination.query.get(des_id)
#     if destination: return jsonify(destination.toDict()) #? if id exists
#     else: return jsonify({"error": "Does not exist"}), 404 #? send data, then custom http status code
# #* http://127.0.0.1:5000/des/id OR in practice: http://127.0.0.1:5000/des/1

# @app.route("/des", methods=["POST"]) #? destinations route, with POST method
# def add_des():
#     data = request.get_json() #? parse data to json
#     newDes = Destination(destination=data["destination"],
#                          country=data["country"],
#                          rating=data["rating"])
#     db.session.add(newDes) #? add new entry to database
#     db.session.commit() #? like git commit
    
#     return jsonify(newDes.toDict()), 201 #? Tell successfully posted data to database

# @app.route("/des/<int:des_id>", methods = ["PUT"])
# def update_destination(des_id):
#     data = request.get_json() #? parse data to json
    
#     destination = Destination.query.get(des_id) #? 
#     if destination:
#         destination.destination = data.get("destination", destination.destination)
#         destination.country = data.get("country", destination.country)
#         destination.rating = data.get("rating", destination.rating)
        
#         db.session.commit() #? commit
#         return jsonify(destination.toDict())
    
#     else: return jsonify({"error": "Does not exist"}), 404
    
# @app.route("/des/<int:des_id>", methods=["DELETE"])
# def deleteDes(des_id):
#     des = Destination.query.get(des_id)
#     if des:
#         db.session.delete(des) #? tap into session and delete entry
#         db.session.commit()
#         return jsonify({"message":"destination was deleted"})
#     else: return jsonify({"error": "Does not exist"}), 404

if __name__ == "__main__": app.run(debug=True) #? print debug and make sure app runs smoothly
