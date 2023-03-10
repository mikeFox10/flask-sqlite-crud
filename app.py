from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///date.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
ma = Marshmallow(app)


class DateM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pub_date = db.Column(db.DateTime)

    def __init__(self, pub_date):
        self.pub_date = pub_date



class DateMSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'pub_date')

user_schema = DateMSchema()
dates_schema = DateMSchema(many=True)


class DateMManager(Resource):
    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            dates = DateM.query.all()
            return jsonify(dates_schema.dump(dates))
        user = DateM.query.get(id)
        return jsonify(user_schema.dump(user))

    @staticmethod
    def post():
        pub_date = datetime.strptime(request.json['pub_date'], '%Y-%m-%d %H:%M:%S')
        user = DateM(pub_date)
        db.session.add(user)
        db.session.commit()
        print(user)
        return jsonify({
            'Message': f'DateM ID = {user.id} inserted.'
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the user ID' })
        
        listId = id.split(',')
        print('listId',listId)

        swDeleted = False
        for idx in listId:
            user = DateM.query.get(idx)
            print(user)
            if user:
                db.session.delete(user)
                db.session.commit()
                swDeleted = True
        if swDeleted:
            return jsonify({
                'Message': f'Items deleted.'
            })
        else: 
            return jsonify({
                'Message': f'Not found'
            })  


api.add_resource(DateMManager, '/api/dates')

if __name__ == '__main__':
    app.run(debug=True)
