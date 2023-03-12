from flask import Flask
from flask_restful import reqparse, Resource, Api
from uuid import uuid4

app = Flask(__name__)
api = Api(app)

base = {"hello": "woraaaald"}

lista = list([{"nome":'arduino uno', 'id': "9c2309dc-13f7-49a9-96c4-cca1186d7cbf"}])

class HelloWorld(Resource):
    def get(self):
        return lista
    def post(self): #create
        parser = reqparse.RequestParser()
        parser.add_argument("nome")
        # parser.add_argument("quant")
        args = parser.parse_args()
        args["id"] = str(uuid4())
        print(args)
        lista.append(args)
        #id = table.insert(args)
        return {"status":"create", "dados":args}
    def put(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        parser.add_argument("nome")
        args = parser.parse_args()
        for item in lista:
            if item["id"] == args["id"]:
                item["nome"] = args["nome"]
                return {"status":"update", "dados":item}
        return {"status":"not found"}
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument("id")
        args = parser.parse_args()
        for item in lista:
            if item["id"] == args["id"]:
                lista.remove(item)
                return{"item removido":args}                


api.add_resource(HelloWorld, "/api/")

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, request

# app = Flask(__name__)

# @app.route("/create", methods=['POST'])
# def create():
#     #return "<p>Hello, world!<p>"
#     if request.method == "POST":
#         return do_the_login()
#     else:
#         return show_the_login_form()
#create read update delete