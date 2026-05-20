from flask import Flask
from config import Config
from models.games import db
from routes.games_routes import game_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)


with app.app_context():
    db.create_all()


app.register_blueprint(game_bp)

if __name__ == '__main__':
    app.run(debug=True)