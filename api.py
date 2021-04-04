from flask import Flask, request, jsonify
import requests
from flask_restplus import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/api/v1/ping', methods=['POST'])
class PingPong(Resource):
    def post(self):
        post_req = request.get_json()
        get_req = post_req['url']
        r = requests.get(url = get_req)
        return r.json()

@api.route('/health', methods=['GET'])
class CheckHealth(Resource):
    def get(self):
        return 'healthy'
        # to be done part

if __name__ == '__main__':
    app.run(host='0.0.0.0')
