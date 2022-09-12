from flask import Flask

from api_initiator.request_schema import api_v1
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "*"}},  supports_credentials=True)

app.register_blueprint(api_v1)



if __name__ == "__main__":
    app.run(debug=True)
