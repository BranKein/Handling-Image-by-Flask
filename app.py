from flask import Flask
from config import FLASK_SECRET
import endpoints

app = Flask(__name__)
app.register_blueprint(endpoints.one_image_blueprint, url_prefix='/one_image')

app.secret_key = FLASK_SECRET


@app.before_first_request
def print_map():
    print(app.url_map)


if __name__ == '__main__':
    app.run()
