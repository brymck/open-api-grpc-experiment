from flask import Flask, json, make_response
from flask_restplus import Api, Resource, fields

app = Flask(__name__)
api = Api(app, version='0.0.1', schemes=['http'])

person = api.model('Person', {
    'name': fields.String(required=True, description="The person's name")
})

greeting = api.model('Greeting', {
    'message': fields.String(required=True, description="The greeting's message")
})


@api.route('/')
@api.response('default', 'Unexpected error')
class HelloWorld(Resource):
    @api.doc('greet')
    @api.expect(person, validate=True)
    @api.marshal_with(greeting, code='200')
    def post(self):
        name = api.payload['name']
        return {'message': f'Hello, {name.title()}!'}


@app.route('/schema')
def dump_schema():
    schema = {
        'host': 'localhost:5000',
        'schemes': ['http'],
    }
    schema.update(api.__schema__)
    return make_response(json.dumps(schema, indent=2, separators=(',', ': ')), 200)
