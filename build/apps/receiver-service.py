from flask import Flask
from flask import jsonify
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@api.route('/api/v1/info', methods=['GET'])
class ReturnInfo(Resource):
    def get(self):
        return jsonify(Receiver='Hello api.py!')

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')


