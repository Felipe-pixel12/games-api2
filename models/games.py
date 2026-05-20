from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Game(db.Model):
    __tablename__ = 'jogos'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    desenvolvedor = db.Column(db.String(100), nullable=False)
    plataforma = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'titulo': self.titulo,
            'genero': self.genero,
            'desenvolvedor': self.desenvolvedor,
            'plataforma': self.plataforma
        }