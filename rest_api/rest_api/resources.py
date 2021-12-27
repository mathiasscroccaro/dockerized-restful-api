from flask import request
from flask_restful import Resource, Api
from rest_api import models, db, app

class User(Resource):
    def get(self):
        username = request.args.get('username')

        m = models.User.query.filter_by(
                    username = username
                ).first()

        if m is None:
            return "Usuário não encontrado"

        return f"Usuário {m.username} {m.email}"

    def post(self):
        username = request.form.get('username')
        email = request.form.get('email')
        
        new_user = models.User(
                    username = username,
                    email = email
                )

        db.session.add(new_user)
        db.session.commit()

        return "Usuário {username} inserido no DB"


api = Api(app)
api.add_resource(User, '/user')
