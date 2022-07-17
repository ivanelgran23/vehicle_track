from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='static')

from app.api.endpoints import main


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
